import os
words_path = './DATA/words.txt'
words_dir = './DATA/words_chunks'
os.makedirs(words_dir, exist_ok=True)

with open(words_path, 'r', encoding='utf-8') as words_file:
  chunk_size = 1800
  chunk = []
  chunk_index = 1

  for line in words_file:
    chunk.append(line)
    if len(chunk) == chunk_size:
      chunk_filename = os.path.join(words_dir, f'words_chunk_{chunk_index}.txt')
      with open(chunk_filename, 'w', encoding='utf-8') as chunk_file:
        chunk_file.writelines(chunk)
      chunk = []
      chunk_index += 1

  # Write any remaining lines in the last chunk
  if chunk:
    chunk_filename = os.path.join(words_dir, f'words_chunk_{chunk_index}.txt')
    with open(chunk_filename, 'w') as chunk_file:
      chunk_file.writelines(chunk)