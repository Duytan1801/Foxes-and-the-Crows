
import os
from openai import OpenAI
import json
import re

client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key="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"
)

system_prompt = """
You are an expert in mathematics and knowledge representation.

I will provide you a section of a math textbook containing LaTeX-formatted mathematical content. Your task is to extract every **statement, definition, claim, theorem, equation, and explicit logical relationship** from the text and present it as a structured **reasoning graph**.

IMPORTANT: The text contains LaTeX formatting commands. Focus on the mathematical content and ignore LaTeX commands like `\Chapter{}`, `\Section{}`, `\Tag{}`, etc. Extract the actual mathematical meaning.

You must treat as a node **every sentence or expression that has mathematical or logical content**, including intermediate reasoning steps, not just highlighted theorems or definitions.

The output must be a JSON array. Each element of the array is a node in the reasoning graph with the following fields:

1. **id** – unique identifier for each statement/concept (e.g., "N1", "N2", "N3", etc.).
2. **type** – one of the following exact strings:
   - "Definition"
   - "Claim"
   - "Theorem"
   - "Statement"
   - "Equation"
   - "Note"
   - "Example"
3. **text** – the actual mathematical content (without LaTeX structural/formatting commands).
4. **dependencies** – list of Node IDs this statement directly depends on or follows from.
5. **equations** – list of equation labels or numbers referenced by this node, if applicable.

---

### Node inclusion

- Extract every statement that has mathematical or logical content, including intermediate reasoning steps.
- If you are unsure whether a sentence is mathematical or logical, include it as a node of type `"Statement"` rather than omitting it.
- Extract standalone equations or formulas as nodes of type `"Equation"`.

---

### Dependencies semantics (VERY IMPORTANT)

A node A depends on node B if, and only if, at least one of the following holds:

1. **Explicit reference to equations or results**
   - A explicitly mentions equation numbers, labels, or names that correspond to B, e.g.:
     - “from equation (19)”
     - “by (21)”
     - “using eq. IV(6)”
   - In that case:
     - Ensure B is a node representing that equation or result.
     - Include B’s `"id"` in A’s `"dependencies"`.
     - Include the label/number in A’s `"equations"` list (e.g., `["(19)"]`, `["IV(6)"]`).

2. **Reference to the immediately preceding equation or result**
   - A uses phrases like “the above equation”, “the previous result”, “this gives”, “hence we obtain”, etc., and is clearly referring to the immediately preceding relevant node.
   - In that case:
     - Include the immediately preceding node’s `"id"` in `"dependencies"`.

3. **Direct local algebraic transformation**
   - A is the direct next algebraic step transforming the expression in B (e.g., rearranging, factoring, differentiating, integrating, or simplifying the same expression).
   - This should be **local**: B is typically the equation or expression just before A in the text.

**Do NOT:**

- Do not infer long-range or implicit logical influence (e.g., “this theorem uses many earlier results”) unless explicitly referenced.
- Do not include dependencies just because earlier definitions or equations are conceptually relevant but not explicitly cited.
- If you are not sure whether B is directly used to obtain A, **do not** list B in `"dependencies"`. It is better to omit a dependency than to guess.

If there are no clear dependencies according to the rules above, use an empty list `[]` for `"dependencies"`.

---

### Equations field

- The `"equations"` field should contain a list of strings with equation labels or numbers **exactly as they appear in the text**, for example:
  - `["(3.1)"]`
  - `["19"]`
  - `["IV(6)"]`
  - `["Eq. (5)"]`
- If the node references multiple equations, include all of them in the list, e.g. `["(19)", "IV(6)"]`.
- If there is no explicit equation label or number referenced, use an empty list `[]`.
- If there is an important equation (display or inline) without a label, still create a node of type `"Equation"` and leave `"equations"` as an empty list.

---

### LaTeX handling

- Ignore LaTeX structural commands such as:
  - `\Chapter{}`, `\Section{}`, `\subsection{}`, `\label{}`, `\tag{}`, `\begin{equation}`, `\end{equation}`, etc.
- Remove LaTeX formatting commands while preserving the mathematical expressions and their structure.
  - For inline or display math, keep the mathematical content. For example:
    - Convert `$\int_0^1 x^2 \, dx$` to either `∫_0^1 x^2 dx` or the plain text string `\int_0^1 x^2 dx`.
- Do **not** invent symbols or change the mathematical meaning.
- Do **not** simplify or alter equations; copy the mathematical content as faithfully as possible, minus LaTeX wrappers.

---

### Type field

- The `"type"` field must be **exactly one of**:
  - `"Definition"`, `"Claim"`, `"Theorem"`, `"Statement"`, `"Equation"`, `"Note"`, `"Example"`.
- Use `"Equation"` for standalone algebraic or analytic expressions, equalities, inequalities, or formulas.
- Use `"Definition"` when the text introduces a new concept, notation, or object.
- Use `"Claim"` for asserted facts or derived results that are not explicitly labeled as theorems.
- Use `"Theorem"` only when the text clearly labels something as a theorem (or proposition, lemma, corollary—if present you may still map these to `"Theorem"`).
- Use `"Statement"` for general mathematical/logical sentences that do not clearly fall into the other categories.
- Use `"Note"` for explanatory comments, remarks, or references such as “compare eq. IV(6)”.
- Use `"Example"` for illustrative examples provided in the text.

---

### Uniqueness and order of IDs

- Each node must have a unique `"id"` following the pattern `"N1"`, `"N2"`, `"N3"`, etc.
- IDs must be:
  - Strictly increasing,
  - Never reused,
  - No gaps due to reuse or reset.
- Do **not** assign `"N1"` to more than one node. Once an ID is used, it must never appear again for a different node.

---

### No fictional content

- Do **not** create or infer content that is not explicitly present in the text.
- Do **not** “repair” unclear or corrupted formulas by guessing.
- Only extract what is actually stated or clearly written in the given text (even if OCR artifacts remain).

---

### Behavior when there is no mathematical content

- If you cannot find any mathematical or logical content in the input text, return an empty array: `[]`.

---

### Output format constraints

- Only output valid JSON.
- The output must be a single JSON array of node objects.
- Do not include any other text, explanations, comments, or markdown formatting outside of the JSON structure.
- The JSON must be properly formatted with:
  - Double quotes for all keys and string values,
  - No trailing commas,
  - No additional wrapping text.
- Do **not** include any description of the task, the prompt, or your own reasoning in the output.
- Do **not** describe what you are doing; only output the extracted nodes.

---

### Example of the desired output format

```json
[
  {
    "id": "N1",
    "type": "Definition",
    "text": "Elliptic integrals are integrals of the form V = ∫ F(X, R) dx, where F is rational and R is a quartic radical.",
    "dependencies": [],
    "equations": ["1"]
  },
  {
    "id": "N2",
    "type": "Claim",
    "text": "All integrals of the form ∫ F(X, R) dx can be reduced to three typical forms.",
    "dependencies": ["N1"],
    "equations": ["2"]
  }
]
```
"""

def chunk_text_semantically(text):
    """
    Chunk text based on semantic boundaries in mathematical content.
    Splits at equation definitions, theorems, definitions, and examples.
    """
    chunks = []
    
    # Define semantic boundary patterns
    boundary_patterns = [
        r'\n\s*\\Tag\{\(',  # Equation tags
        r'\n\s*\\(?:Chapter|Section|Subsection)\{',  # Section boundaries
        r'\n\s*\\(?:First|Second|Third)\{',  # Paragraph starters
        r'\n\s*#{1,6}\s+',  # Markdown headers
        r'\n\s*\[(?=\d+\)|\w+\.\d+)',  # Numbered lists/items
        r'\n\s*\\(?:begin|end)\{',  # LaTeX environments
        r'\n\s*\$\$',  # Display math delimiters
    ]
    
    # Combine patterns into a single regex
    combined_pattern = '|'.join(boundary_patterns)
    split_points = [0]
    
    # Find all boundary positions
    import re
    for match in re.finditer(combined_pattern, text):
        split_points.append(match.start())
    
    # Add end of text as final split point
    split_points.append(len(text))
    
    # Create chunks based on split points
    for i in range(len(split_points) - 1):
        start = split_points[i]
        end = split_points[i + 1]
        chunk = text[start:end].strip()
        
        # Skip empty chunks
        if chunk:
            # If chunk is too large, split it further by paragraphs
            if len(chunk) > 1500:
                paragraphs = re.split(r'\n\s*\n', chunk)
                sub_chunks = []
                current_sub_chunk = ""
                
                for paragraph in paragraphs:
                    if len(current_sub_chunk) + len(paragraph) > 1500 and current_sub_chunk:
                        sub_chunks.append(current_sub_chunk.strip())
                        current_sub_chunk = paragraph
                    else:
                        if current_sub_chunk:
                            current_sub_chunk += "\n\n" + paragraph
                        else:
                            current_sub_chunk = paragraph
                
                if current_sub_chunk:
                    sub_chunks.append(current_sub_chunk.strip())
                
                chunks.extend(sub_chunks)
            else:
                chunks.append(chunk)
    
    # Merge small chunks with previous chunks to maintain minimum size
    merged_chunks = []
    current_merged_chunk = ""
    
    for chunk in chunks:
        if len(current_merged_chunk) + len(chunk) < 800:
            current_merged_chunk += "\n\n" + chunk if current_merged_chunk else chunk
        else:
            if current_merged_chunk:
                merged_chunks.append(current_merged_chunk)
            current_merged_chunk = chunk
    
    if current_merged_chunk:
        merged_chunks.append(current_merged_chunk)
    
    return merged_chunks


def extract_chapters_and_sections(content):
    """Extract chapters and sections from the markdown content respecting natural boundaries."""
    chapters = []
    
    # Split content by chapters (using LaTeX \Chapter{...}{...} pattern)
    # Use positive lookahead to split at chapter boundaries but include the chapter header
    chapter_pattern = r'(?=\\Chapter\{[^}]+\}\{[^}]+\})'
    chapter_parts = re.split(chapter_pattern, content)
    
    # The first part might be content before the first chapter
    if chapter_parts and chapter_parts[0].strip():
        # Check if the first part starts with a chapter header
        first_chapter_match = re.search(r'(\\Chapter\{[^}]+\}\{[^}]+\})', chapter_parts[0])
        if first_chapter_match:
            # First part contains a chapter header at the beginning
            chapter_header = first_chapter_match.group(1)
            chapter_content = chapter_parts[0][first_chapter_match.end():].strip()
            chapters.append({
                'header': chapter_header,
                'content': chapter_content
            })
        else:
            # This is introductory content before the first chapter
            if chapter_parts[0].strip():
                chapters.append({
                    'header': 'Introductory Chapter',
                    'content': chapter_parts[0].strip()
                })
    
    # Process remaining chapters
    for i in range(1, len(chapter_parts)):
        part = chapter_parts[i]
        chapter_match = re.search(r'(\\Chapter\{[^}]+\}\{[^}]+\})', part)
        if chapter_match:
            chapter_header = chapter_match.group(1)
            chapter_content = part[chapter_match.end():].strip()
            chapters.append({
                'header': chapter_header,
                'content': chapter_content
            })
        elif part.strip():
            # This should not happen if the pattern works correctly
            chapters.append({
                'header': f'Chapter_{i}',
                'content': part.strip()
            })
    
    return chapters

def chunk_by_semantic_boundaries(text, max_chunk_size=1500):
    """Chunk text by semantic boundaries while respecting size constraints."""
    chunks = []
    
    # Split by sections within the text using positive lookahead
    section_pattern = r'(?=\\Section\{[^}]+\})'
    section_parts = re.split(section_pattern, text)
    
    # Process sections
    for i, part in enumerate(section_parts):
        if not part.strip():
            continue
            
        section_match = re.search(r'(\\Section\{[^}]+\})', part)
        if section_match:
            section_header = section_match.group(1)
            section_content = part[section_match.end():].strip()
            
            if section_content:
                section_chunks = chunk_section_content(section_content, max_chunk_size)
                for chunk in section_chunks:
                    chunks.append({
                        'section_header': section_header,
                        'content': chunk
                    })
        else:
            # This is content without a section header (could be chapter intro)
            section_chunks = chunk_section_content(part.strip(), max_chunk_size)
            for chunk in section_chunks:
                chunks.append({
                    'section_header': 'No section',
                    'content': chunk
                })
    
    return chunks

def chunk_section_content(text, max_chunk_size=1500):
    """Chunk section content by semantic boundaries while respecting size limits."""
    chunks = []
    
    # Define semantic boundary patterns for mathematical content
    boundary_patterns = [
        r'\n\s*\\Tag\{\(',  # Equation tags
        r'\n\s*\$\$',  # Display math delimiters
        r'\n\s*\\begin\{',  # LaTeX environment starts
        r'\n\s*\\end\{',  # LaTeX environment ends
        r'\n\s*#{1,6}\s+',  # Markdown headers
        r'\n\s*\[(?=\d+\)|\w+\.\d+)',  # Numbered lists/items
    ]
    
    combined_pattern = '|'.join(boundary_patterns)
    split_points = [0]
    
    # Find all boundary positions
    for match in re.finditer(combined_pattern, text):
        split_points.append(match.start())
    
    # Add end of text as final split point
    split_points.append(len(text))
    
    # Create chunks based on split points
    for i in range(len(split_points) - 1):
        start = split_points[i]
        end = split_points[i + 1]
        chunk = text[start:end].strip()
        
        if chunk:
            # If chunk is too large, split by paragraphs
            if len(chunk) > max_chunk_size:
                paragraphs = re.split(r'\n\s*\n', chunk)
                sub_chunks = []
                current_sub_chunk = ""
                
                for paragraph in paragraphs:
                    if len(current_sub_chunk) + len(paragraph) > max_chunk_size and current_sub_chunk:
                        sub_chunks.append(current_sub_chunk.strip())
                        current_sub_chunk = paragraph
                    else:
                        if current_sub_chunk:
                            current_sub_chunk += "\n\n" + paragraph
                        else:
                            current_sub_chunk = paragraph
                
                if current_sub_chunk:
                    sub_chunks.append(current_sub_chunk.strip())
                
                chunks.extend(sub_chunks)
            else:
                chunks.append(chunk)
    
    # Merge small chunks to maintain minimum size
    merged_chunks = []
    current_merged_chunk = ""
    
    for chunk in chunks:
        if len(current_merged_chunk) + len(chunk) < 800:
            current_merged_chunk += "\n\n" + chunk if current_merged_chunk else chunk
        else:
            if current_merged_chunk:
                merged_chunks.append(current_merged_chunk)
            current_merged_chunk = chunk
    
    if current_merged_chunk:
        merged_chunks.append(current_merged_chunk)
    
    return merged_chunks

def process_section_with_context(content, section_header="", previous_context=""):
    """Process a section with context preservation for relationship extraction."""
    print(f"Processing section: {section_header}")
    
    # Prepare the content with context - limit context to avoid overwhelming the model
    if previous_context:
        # Use only the most recent context (last 500 characters)
        recent_context = previous_context[-500:] if len(previous_context) > 500 else previous_context
        full_content = f"Previous context: {recent_context}\n\n--- CURRENT SECTION ---\n\n{content}"
    else:
        full_content = content
    
    # Clean LaTeX content to make it more readable for the AI
    # Remove excessive LaTeX formatting while keeping mathematical content
    cleaned_content = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', full_content)  # Remove LaTeX commands like \Chapter{}
    cleaned_content = re.sub(r'\\[a-zA-Z]+', '', cleaned_content)  # Remove other LaTeX commands
    cleaned_content = re.sub(r'\$\$([^$]+)\$\$', r'\1', cleaned_content)  # Remove display math delimiters
    cleaned_content = re.sub(r'\$([^$]+)\$', r'\1', cleaned_content)  # Remove inline math delimiters
    
    try:
        completion = client.chat.completions.create(
            model="qwen/qwen3-next-80b-a3b-thinking",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Extract reasoning graph from the following mathematical text. Focus on the mathematical concepts, definitions, theorems, and relationships:\n\n{cleaned_content}"}
            ],
            temperature=0.0,
            top_p=0.7,
            max_tokens=100000,
            stream=False
        )
        
        response_content = completion.choices[0].message.content
        
        # Improved JSON extraction with multiple fallback strategies
        try:
            # Strategy 1: Look for JSON array pattern (complete or partial)
            json_match = re.search(r'\[\s*\{.*?\}\s*\]', response_content, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                # Clean up potential JSON issues
                json_str = re.sub(r',\s*\]', ']', json_str)  # Remove trailing commas
                json_str = re.sub(r',\s*\}', '}', json_str)  # Remove trailing commas in objects
                try:
                    nodes = json.loads(json_str)
                    print(f"Successfully extracted {len(nodes)} nodes")
                    return nodes
                except json.JSONDecodeError:
                    # Try to fix incomplete JSON by adding closing brackets
                    if not json_str.endswith(']'):
                        json_str += ']'
                    try:
                        nodes = json.loads(json_str)
                        print(f"Successfully extracted {len(nodes)} nodes (fixed incomplete array)")
                        return nodes
                    except json.JSONDecodeError:
                        pass
            
            # Strategy 2: Look for JSON object pattern
            json_match = re.search(r'\{\s*"type".*?\}\s*\]', response_content, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                json_str = re.sub(r',\s*\]', ']', json_str)
                json_str = re.sub(r',\s*\}', '}', json_str)
                try:
                    nodes = json.loads(json_str)
                    print(f"Successfully extracted {len(nodes)} nodes")
                    return nodes
                except json.JSONDecodeError:
                    pass
            
            # Strategy 3: Try to parse the entire response as JSON
            try:
                nodes = json.loads(response_content.strip())
                print(f"Successfully parsed entire response as JSON: {len(nodes)} nodes")
                return nodes
            except json.JSONDecodeError:
                pass
                
            # Strategy 4: Look for code blocks with JSON
            code_block_match = re.search(r'```json\s*(.*?)\s*```', response_content, re.DOTALL)
            if code_block_match:
                json_str = code_block_match.group(1)
                try:
                    nodes = json.loads(json_str)
                    print(f"Successfully extracted JSON from code block: {len(nodes)} nodes")
                    return nodes
                except json.JSONDecodeError:
                    pass
            
            # Strategy 5: Look for incomplete JSON and try to complete it
            # Check if response starts with [ but doesn't end properly
            if response_content.strip().startswith('[') and not response_content.strip().endswith(']'):
                # Try to add closing bracket
                try:
                    json_str = response_content.strip() + ']'
                    nodes = json.loads(json_str)
                    print(f"Successfully extracted {len(nodes)} nodes (completed incomplete array)")
                    return nodes
                except json.JSONDecodeError:
                    pass
            
            # Strategy 6: Extract individual JSON objects and combine
            json_objects = re.findall(r'\{\s*"[^"]*"[^}]*\}', response_content)
            if json_objects:
                try:
                    # Combine individual objects into an array
                    json_str = '[' + ','.join(json_objects) + ']'
                    nodes = json.loads(json_str)
                    print(f"Successfully extracted {len(nodes)} nodes from individual objects")
                    return nodes
                except json.JSONDecodeError:
                    pass
            
            print(f"Warning: Could not find valid JSON in response")
            print(f"Response preview: {response_content[:500]}...")
            return []
            
        except json.JSONDecodeError as e:
            print(f"Warning: Could not parse JSON response")
            print(f"Error: {str(e)}")
            print(f"Problematic JSON: {response_content[:500]}...")
            return []
    except Exception as e:
        print(f"Error calling API: {str(e)}")
        return []

def main():
    """Main function to process markdown_file.md directly with intelligent chunking."""
    markdown_file = "markdown_file.md"
    all_results = {}
    
    print(f"Processing markdown file: {markdown_file}")
    
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract chapters from the content
    chapters = extract_chapters_and_sections(content)
    print(f"Found {len(chapters)} chapters in the document")
    
    total_sections_processed = 0
    
    # Keep track of context from previous sections
    previous_context = ""
    
    for i, chapter in enumerate(chapters):
        chapter_header = chapter['header']
        chapter_content = chapter['content']
        
        print(f"Processing chapter {i+1}: {chapter_header}")
        
        # Extract sections and chunk the chapter content
        chunks = chunk_by_semantic_boundaries(chapter_content)
        
        chapter_nodes = []
        for j, chunk_info in enumerate(chunks):
            chunk_content = chunk_info['content']
            section_header = chunk_info.get('section_header', 'No section')
            
            print(f"  Processing section {j+1}/{len(chunks)} (Section: {section_header})")
            
            # Process section with context
            section_nodes = process_section_with_context(chunk_content, section_header, previous_context)
            chapter_nodes.extend(section_nodes)
            
            # Update context with a summary of the current section for next iteration
            # For now, we'll use the first and last few sentences as context
            lines = chunk_content.split('\n')
            if len(lines) > 10:
                # Take first 3 and last 3 lines as context
                context_lines = lines[:3] + lines[-3:]
                previous_context = '\n'.join(context_lines)
            else:
                previous_context = chunk_content
        
        all_results[f"chapter_{i+1}_{chapter_header}"] = chapter_nodes
        total_sections_processed += len(chunks)
        print(f"Completed chapter {i+1}, processed {len(chunks)} sections")
    
    output_file = "reasoning_graph_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"Reasoning graph extraction completed. Processed {total_sections_processed} sections across {len(chapters)} chapters. Results saved to {output_file}")

if __name__ == "__main__":
    main()
