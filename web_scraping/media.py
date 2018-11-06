import webbrowser, sys

if len(sys.argv) > 1:
    # address = sys.argv[1:]
    address = ' '.join(sys.argv[1:])
    # print(address)

webbrowser.open('https://' + address)