## Not solved

cases = int(input())
for case in range(cases):
    n = int(input())
    binary = input()
    binary2 = binary
    respuesta = []
    if(binary == binary[::-1]):
        print(0)
        continue
    else:
        for i in range(n):
            if(binary[i])== '0':
                binary = binary.replace("0","")
                respuesta.append(i)
        if(binary == binary[::-1]):
            print(len(respuesta))
            print(binary)
        else:
            for i in range(n):
                if(binary2[i])== '0':
                    binary2 = binary2.replace("0","")
                    respuesta.append(i)
                if(binary2 == binary2[::-1]):
                    print(len(respuesta))
                    print(binary)