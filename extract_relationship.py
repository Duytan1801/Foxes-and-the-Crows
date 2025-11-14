import os
import json
import re
from typing import List, Dict, Any, Tuple
from openai import OpenAI

# =========================
#  API CLIENT
# =========================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"  # <<< REPLACE WITH YOUR KEY
)

# =========================
#  SYSTEM PROMPT
# =========================

system_prompt = """
You are an expert in mathematics and knowledge representation.

I will provide you a section of a math textbook containing LaTeX-formatted mathematical content. Your task is to extract every **statement, definition, claim, theorem, equation, and explicit logical relationship** from the text and present it as a structured **reasoning graph**.

IMPORTANT: The text contains LaTeX formatting commands. Focus on the mathematical content and ignore LaTeX commands like \\Chapter{}, \\Section{}, \\Tag{}, etc. Extract the actual mathematical meaning.

You must treat as a node **every sentence or expression that has mathematical or logical content**, including intermediate reasoning steps, not just highlighted theorems or definitions.

The output must be a JSON array. Each element of the array is a node in the reasoning graph with the following fields:

1. "id" – unique identifier for each statement/concept (e.g., "N1", "N2", "N3", etc.).
2. "type" – one of the following exact strings:
   - "Definition"
   - "Claim"
   - "Theorem"
   - "Statement"
   - "Equation"
   - "Note"
   - "Example"
3. "text" – the actual mathematical content (without LaTeX structural/formatting commands).
4. "dependencies" – list of Node IDs this statement directly depends on or follows from.
5. "equations" – list of equation labels or numbers referenced by this node, if applicable.

---

### Node inclusion

- Extract every statement that has mathematical or logical content, including intermediate reasoning steps.
- If you are unsure whether a sentence is mathematical or logical, include it as a node of type "Statement" rather than omitting it.
- Extract standalone equations or formulas as nodes of type "Equation".

---

### Dependencies semantics (VERY IMPORTANT)

A node A depends on node B if, and only if, at least one of the following holds:

1. Explicit reference to equations or results
   - A explicitly mentions equation numbers, labels, or names that correspond to B, e.g.:
     - "from equation (19)"
     - "by (21)"
     - "using eq. IV(6)"
   - In that case:
     - Ensure B is a node representing that equation or result.
     - Include B's "id" in A's "dependencies".
     - Include the label/number in A's "equations" list (e.g., ["(19)"], ["IV(6)"]).

2. Reference to the immediately preceding equation or result
   - A uses phrases like "the above equation", "the previous result", "this gives", "hence we obtain", etc., and is clearly referring to the immediately preceding relevant node.
   - In that case:
     - Include the immediately preceding node's "id" in "dependencies".

3. Direct local algebraic transformation
   - A is the direct next algebraic step transforming the expression in B (e.g., rearranging, factoring, differentiating, integrating, or simplifying the same expression).
   - This should be local: B is typically the equation or expression just before A in the text.

Do NOT:
- Do not infer long-range or implicit logical influence (e.g., "this theorem uses many earlier results") unless explicitly referenced.
- Do not include dependencies just because earlier definitions or equations are conceptually relevant but not explicitly cited.
- If you are not sure whether B is directly used to obtain A, do not list B in "dependencies". It is better to omit a dependency than to guess.

If there are no clear dependencies according to the rules above, use an empty list [] for "dependencies".

---

### Equations field

- The "equations" field should contain a list of strings with equation labels or numbers exactly as they appear in the text, for example:
  - ["(3.1)"]
  - ["19"]
  - ["IV(6)"]
  - ["Eq. (5)"]
- If the node references multiple equations, include all of them in the list, e.g. ["(19)", "IV(6)"].
- If there is no explicit equation label or number referenced, use an empty list [].
- If there is an important equation (display or inline) without a label, still create a node of type "Equation" and leave "equations" as an empty list.

---

### LaTeX handling

- Ignore LaTeX structural commands such as:
  - \\Chapter{}, \\Section{}, \\Subsection{}, \\subsection{}, \\label{}, \\Tag{}, \\begin{...}, \\end{...}, etc.
- Remove LaTeX formatting commands while preserving the mathematical expressions and their structure.
  - For inline or display math, keep the mathematical content. For example:
    - Convert "$\\int_0^1 x^2 \\, dx$" to either "∫_0^1 x^2 dx" or the plain text string "\\int_0^1 x^2 dx".
- Do not invent symbols or change the mathematical meaning.
- Do not simplify or alter equations; copy the mathematical content as faithfully as possible, minus LaTeX wrappers.

---

### Type field

- The "type" field must be exactly one of:
  - "Definition", "Claim", "Theorem", "Statement", "Equation", "Note", "Example".
- Use "Equation" for standalone algebraic or analytic expressions, equalities, inequalities, or formulas.
- Use "Definition" when the text introduces a new concept, notation, or object.
- Use "Claim" for asserted facts or derived results that are not explicitly labeled as theorems.
- Use "Theorem" only when the text clearly labels something as a theorem (or proposition, lemma, corollary—these may also be mapped to "Theorem").
- Use "Statement" for general mathematical/logical sentences that do not clearly fall into the other categories.
- Use "Note" for explanatory comments, remarks, or references such as "compare eq. IV(6)".
- Use "Example" for illustrative examples provided in the text.

---

### Uniqueness and order of IDs

- Each node must have a unique "id" following the pattern "N1", "N2", "N3", etc.
- IDs must be:
  - Strictly increasing,
  - Never reused,
  - No gaps due to reuse or reset.
- Do not assign "N1" to more than one node. Once an ID is used, it must never appear again for a different node.

---

### No fictional content

- Do not create or infer content that is not explicitly present in the text.
- Do not "repair" unclear or corrupted formulas by guessing.
- Only extract what is actually stated or clearly written in the given text (even if OCR artifacts remain).

---

### Behavior when there is no mathematical content

- If you cannot find any mathematical or logical content in the input text, return an empty array: [].

---

### Output format constraints

- Only output valid JSON.
- The output must be a single JSON array of node objects.
- Do not include any other text, explanations, comments, or markdown formatting outside of the JSON structure.
- The JSON must be properly formatted with:
  - Double quotes for all keys and string values,
  - No trailing commas,
  - No additional wrapping text.
- Do not include any description of the task, the prompt, or your own reasoning in the output.
- Do not describe what you are doing; only output the extracted nodes.
"""

# =========================
#  LATEX CLEANING
# =========================

def clean_latex_for_model(text: str) -> str:
    """
    Remove structural LaTeX commands while preserving mathematical content.
    Do NOT strip generic math commands like \int, \sin, etc.
    """
    # Remove chapter/section-level structural commands entirely
    text = re.sub(r'\\(Chapter|Section|Subsection|subsection|paragraph|subparagraph)\{[^}]*\}', '', text)

    # Remove \label{...}, \Tag{...}
    text = re.sub(r'\\(label|Tag)\{[^}]*\}', '', text)

    # Remove begin/end of environments but keep inner content
    text = re.sub(r'\\begin\{[^}]*\}', '', text)
    text = re.sub(r'\\end\{[^}]*\}', '', text)

    # Remove display math delimiters $$...$$, keep content
    text = re.sub(r'\$\$([^$]+)\$\$', r'\1', text, flags=re.DOTALL)

    # Remove inline math delimiters $...$, keep content
    text = re.sub(r'\$([^$]+)\$', r'\1', text, flags=re.DOTALL)

    # Compress excessive blank lines
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)

    return text.strip()

# =========================
#  SEMANTIC CHUNKING
# =========================

def extract_chapters(content: str) -> List[Dict[str, str]]:
    """
    Extract chapter blocks from LaTeX-like content based on \Chapter{...}{...}.
    Returns a list of dicts with 'header' and 'content'.
    """
    chapters = []
    chapter_pattern = r'(?=\\Chapter\{[^}]+\}\{[^}]+\})'
    parts = re.split(chapter_pattern, content)

    # If there is content before the first \Chapter, treat it as an intro
    if parts and parts[0].strip():
        chapters.append({
            "header": "Introductory Chapter",
            "content": parts[0].strip()
        })

    for i in range(1, len(parts)):
        part = parts[i]
        m = re.search(r'(\\Chapter\{[^}]+\}\{[^}]+\})', part)
        if m:
            header = m.group(1)
            chapter_content = part[m.end():].strip()
            chapters.append({
                "header": header,
                "content": chapter_content
            })
        else:
            if part.strip():
                chapters.append({
                    "header": f"Chapter_{i}",
                    "content": part.strip()
                })

    return chapters


def split_into_sections(chapter_text: str) -> List[Dict[str, str]]:
    """
    Split chapter content into sections by \Section{...}.
    Returns list of {section_header, content}.
    """
    chunks = []
    section_pattern = r'(?=\\Section\{[^}]+\})'
    parts = re.split(section_pattern, chapter_text)

    for part in parts:
        if not part.strip():
            continue
        m = re.search(r'(\\Section\{[^}]+\})', part)
        if m:
            header = m.group(1)
            content = part[m.end():].strip()
            if content:
                chunks.append({"section_header": header, "content": content})
        else:
            # Content without explicit section header
            chunks.append({"section_header": "No section", "content": part.strip()})

    return chunks


def clever_semantic_chunks(text: str, max_chunk_size: int = 1500, min_chunk_size: int = 600) -> List[str]:
    """
    More clever semantic chunking:
    1. First split by strong math/structure boundaries: equation tags, display math, environments.
    2. Within each piece, split by paragraph boundaries if too large.
    3. Then merge small neighboring chunks to reach at least min_chunk_size where possible.
    """
    # Strong boundaries
    boundary_patterns = [
        r'\n\s*\\Tag\{\(',        # equation tags
        r'\n\s*\\tag\{',          # generic tag
        r'\n\s*\$\$',             # display math
        r'\n\s*\\\[\s*',          # \[
        r'\n\s*\\\]\s*',          # \]
        r'\n\s*\\begin\{[^}]*\}', # environments
        r'\n\s*\\end\{[^}]*\}',
        r'\n\s*%.*$',             # LaTeX comments
    ]
    combined = '|'.join(boundary_patterns)

    split_points = [0]
    for m in re.finditer(combined, text, flags=re.MULTILINE):
        split_points.append(m.start())
    split_points.append(len(text))

    raw_chunks = []
    for i in range(len(split_points) - 1):
        start = split_points[i]
        end = split_points[i+1]
        chunk = text[start:end].strip()
        if not chunk:
            continue

        if len(chunk) > max_chunk_size:
            # Further split by blank line/paragraphs
            paragraphs = re.split(r'\n\s*\n', chunk)
            current = ""
            for p in paragraphs:
                p = p.strip()
                if not p:
                    continue
                if len(current) + len(p) > max_chunk_size and current:
                    raw_chunks.append(current.strip())
                    current = p
                else:
                    current = (current + "\n\n" + p) if current else p
            if current.strip():
                raw_chunks.append(current.strip())
        else:
            raw_chunks.append(chunk)

    # Merge small chunks
    merged = []
    current = ""
    for c in raw_chunks:
        if not current:
            current = c
            continue
        if len(current) < min_chunk_size and len(current) + len(c) <= max_chunk_size:
            current = current + "\n\n" + c
        else:
            merged.append(current.strip())
            current = c
    if current.strip():
        merged.append(current.strip())

    return merged


def chunk_by_semantic_boundaries(chapter_content: str,
                                 max_chunk_size: int = 1500,
                                 min_chunk_size: int = 600) -> List[Dict[str, str]]:
    """
    Take a chapter's content, split into sections, then each section is split into semantic chunks.
    Returns list of {section_header, content}.
    """
    result_chunks = []
    sections = split_into_sections(chapter_content)

    for sec in sections:
        header = sec["section_header"]
        text = sec["content"]
        semantic_chunks = clever_semantic_chunks(text, max_chunk_size, min_chunk_size)
        for sc in semantic_chunks:
            result_chunks.append({
                "section_header": header,
                "content": sc
            })

    return result_chunks

# =========================
#  MODEL CALL & JSON PARSING
# =========================

def parse_model_json(response_content: str) -> List[Dict[str, Any]]:
    """
    Robust but simple JSON extraction:
    1. Try parse entire content.
    2. Fallback: first JSON array substring.
    """
    response_content = response_content.strip()

    # Try full parse
    try:
        data = json.loads(response_content)
        if isinstance(data, list):
            return data
    except json.JSONDecodeError:
        pass

    # Try extract first array
    m = re.search(r'\[\s*\{.*\}\s*\]', response_content, re.DOTALL)
    if m:
        json_str = m.group(0)
        try:
            data = json.loads(json_str)
            if isinstance(data, list):
                return data
        except json.JSONDecodeError:
            pass

    print("Warning: could not parse JSON from model response.")
    print("Response preview:", response_content[:500])
    return []


def process_section_chunk(chunk_content: str,
                          section_header: str = "") -> List[Dict[str, Any]]:
    """
    Process a single semantic chunk with the model.
    """
    print(f"    -> Processing chunk (section: {section_header}, length: {len(chunk_content)} chars)")
    cleaned_content = clean_latex_for_model(chunk_content)

    user_msg = (
        "Extract reasoning graph from the following mathematical text. "
        "Only extract nodes from the given text; do not use any external knowledge.\n\n"
        + cleaned_content
    )

    try:
        completion = client.chat.completions.create(
            model="qwen/qwen3-next-80b-a3b-thinking",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.0,
            top_p=0.7,
            max_tokens=100000,
            stream=False
        )
        response_content = completion.choices[0].message.content
        nodes = parse_model_json(response_content)
        print(f"    <- Extracted {len(nodes)} nodes")
        return nodes
    except Exception as e:
        print("Error calling API:", str(e))
        return []

# =========================
#  ID RENAMING (GLOBAL)
# =========================

def renumber_nodes(nodes: List[Dict[str, Any]],
                   start_index: int) -> Tuple[List[Dict[str, Any]], int]:
    """
    Renumber node IDs to be globally unique: N{start_index}, N{start_index+1}, ...
    Dependencies are remapped if they refer to old IDs present in this chunk.
    """
    new_nodes: List[Dict[str, Any]] = []
    id_map: Dict[str, str] = {}
    current = start_index

    # First pass: assign new ids
    for node in nodes:
        old_id = str(node.get("id", "")).strip()
        new_id = f"N{current}"
        id_map[old_id] = new_id
        node["id"] = new_id
        current += 1
        new_nodes.append(node)

    # Second pass: remap dependencies
    for node in new_nodes:
        deps = node.get("dependencies", [])
        if not isinstance(deps, list):
            deps = []
        remapped = [id_map[d] for d in deps if d in id_map]
        node["dependencies"] = remapped

    return new_nodes, current

# =========================
#  MAIN PIPELINE
# =========================

def main():
    markdown_file = "markdown_file.md"
    output_file = "reasoning_graph_results.json"

    print(f"Loading file: {markdown_file}")
    with open(markdown_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Extract chapters
    chapters = extract_chapters(content)
    print(f"Found {len(chapters)} chapter blocks")

    all_results: Dict[str, Any] = {}
    global_id_counter = 1
    total_chunks = 0

    # 2. Process each chapter
    for ci, chapter in enumerate(chapters, start=1):
        chapter_header = chapter["header"]
        chapter_content = chapter["content"]
        print(f"\n=== Processing Chapter {ci}: {chapter_header} ===")

        # 3. Chunk by semantic boundaries inside chapter
        chunks = chunk_by_semantic_boundaries(chapter_content,
                                              max_chunk_size=1500,
                                              min_chunk_size=600)
        print(f"  Chapter {ci}: {len(chunks)} semantic chunks")

        chapter_nodes: List[Dict[str, Any]] = []

        for j, chunk_info in enumerate(chunks, start=1):
            section_header = chunk_info["section_header"]
            chunk_text = chunk_info["content"]

            print(f"  - Chunk {j}/{len(chunks)} (Section: {section_header})")
            nodes = process_section_chunk(chunk_text, section_header)
            nodes, global_id_counter = renumber_nodes(nodes, global_id_counter)
            chapter_nodes.extend(nodes)

        all_results[f"chapter_{ci}"] = {
            "header": chapter_header,
            "nodes": chapter_nodes
        }
        total_chunks += len(chunks)
        print(f"Completed Chapter {ci}: {len(chapter_nodes)} nodes")

    # 4. Save results
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"\nReasoning graph extraction completed.")
    print(f"Processed {total_chunks} chunks across {len(chapters)} chapters.")
    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()