def create_codon_dict(file_path):
    codon_dict = {}
    
    try:
        with open(file_path, 'r') as file:
            rows = file.readlines()
            
    except FileNotFoundError:
        return None 

    for row in rows:
        cells = row.strip().split('\t')
        
        if len(cells) >= 3:
            codon = cells[0]          
            amino_acid_abbr = cells[2]  
            
            codon_dict[codon] = amino_acid_abbr
    
    return codon_dict

def test_create_codon_dict():
    result = create_codon_dict("data/codons.txt")

    if result is None:
        print("Test Failed: הפונקציה החזירה None.")
        return

    assert result['AAA'] == 'K', f"Test Failed: 'AAA' should map to 'K', got {result.get('AAA')}"
    assert result['AAC'] == 'N', f"Test Failed: 'AAC' should map to 'N', got {result.get('AAC')}"
    assert result['ACA'] == 'T', f"Test Failed: 'ACA' should map to 'T', got {result.get('ACA')}"
    assert result['ACC'] == 'T', f"Test Failed: 'ACC' should map to 'T', got {result.get('ACC')}"
    assert result['UAA'] == '*', f"Test Failed: 'UAA' should map to '*', got {result.get('UAA')}"

    print("✅ All tests passed successfully.")

# test_create_codon_dict()



