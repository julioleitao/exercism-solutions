def distance(strand_a, strand_b):
  if len(strand_a) != len(strand_b):
    raise ValueError("Strands with different length it is not supported")

  count = 0

  for index in range(len(strand_a)):
    if strand_a[index] != strand_b[index]:
      count += 1

  return count

