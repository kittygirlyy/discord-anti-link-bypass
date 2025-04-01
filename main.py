import pyperclip

def convert_utf8_to_hex(s):
    return s.encode('utf-8').hex()

def add_percent_between_hex(hex_string):
    return '%'.join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))

def legacy_format(link):
    if not link.startswith('http'):
        link = 'https://' + link
    legacy_link = link.replace('/', '\\/')
    return legacy_link

def modern_format(link):
    slash_index = link.find('/') + 1
    if slash_index == 0 or len(link) < 7 or link[6] != '/':
        path = link
    else:
        path = link[8:]
    ascii_to_hex = add_percent_between_hex(convert_utf8_to_hex(path)).replace('%2f', '/')
    return f"<ht\ntp\ns:/\\%{ascii_to_hex}\n>"

def start():
    try:
        while True:
            format_choice = input('[=] Use legacy format (like https:\\/\\/8086.re)? [y/N]: ').strip().lower()
            use_legacy = format_choice == 'y'

            link = input('[=] Enter link to send (example: 8086.re): ').strip()

            if not link:
                print('[KO] No link entered. Exiting...')
                break

            result = legacy_format(link) if use_legacy else modern_format(link)
            pyperclip.copy(result)

            print('[OK] Copied to clipboard!\n')
            print(result)

    except KeyboardInterrupt:
        print("\n[EXIT] Program closed.")

if __name__ == '__main__':
    start()
