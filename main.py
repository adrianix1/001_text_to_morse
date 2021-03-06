morse_dict = {'A': '·–',
              'B': '–···',
              'C': '–·–·',
              'D': '–··',
              'E': '·',
              'F': '··–·',
              'G': '––·',
              'H': '····',
              'I': '··',
              'J': '·–––',
              'K': '–·–',
              'L': '·–··',
              'M': '––',
              'N': '–·',
              'O': '–––',
              'P': '·––·',
              'Q': '––·–',
              'R': '·–·',
              'S': '···',
              'T': '–',
              'U': '··–',
              'V': '···–',
              'W': '·––',
              'X': '–··–',
              'Y': '–·––',
              'Z': '––··',
              '1': '·––––',
              '2': '··–––',
              '3': '···––',
              '4': '····–',
              '5': '·····',
              '6': '–····',
              '7': '––···',
              '8': '–––··',
              '9': '––––·',
              '0': '–––––',
              '.': '·–·–·–',
              ',': '––··––'}
print('''████████╗███████╗██╗  ██╗████████╗    ████████╗ ██████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝
   ██║   █████╗   ╚███╔╝    ██║          ██║   ██║   ██║    ██╔████╔██║██║   ██║██████╔╝███████╗█████╗  
   ██║   ██╔══╝   ██╔██╗    ██║          ██║   ██║   ██║    ██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝  
   ██║   ███████╗██╔╝ ██╗   ██║          ██║   ╚██████╔╝    ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝\n''')

print('Welcome in "text to morse code converter"!')

end_program = False
while not end_program:
    user_input = input('Write Your text: ').upper()
    output = []

    for symbol in user_input:
        if symbol not in morse_dict:
            pass
        else:
            output.append(morse_dict[symbol])
    print('Here is Your text in morse code: ')

    print(' '.join(str(elm) for elm in output))

    end_program = input('Do You want to convert another text? (y/n): ')
    if end_program.lower() == 'y':
        end_program = False
    else:
        end_program = True
print("Bye!")
