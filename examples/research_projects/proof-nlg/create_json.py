

if __name__=='__main__':
    fp1 = open('proofs.txt')
    fp2 = open('explanations.txt')
    fp3 = open('data.json', 'w')

    proofline = fp1.readline().strip()
    explain = fp2.readline().strip()

    # Read until EOF
    while proofline != "":
        proof = proofline
        proofline = fp1.readline().strip()
        while proofline != "":   # Proofs are on multiple lines, separated by an empty line
            proof += " " + proofline
            proofline = fp1.readline().strip()

        fp3.write('{"text": "' + proof + '", "summary": "' + explain + '"}\n')
        proofline = fp1.readline().strip()
        _ = fp2.readline() # Skip empty line between entries
        explain = fp2.readline().strip()


    fp3.close()

