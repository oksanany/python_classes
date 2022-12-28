class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        pass

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        pass

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        pass

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        pass

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    start_file = open(file_name, encoding='utf-8')
    content = start_file.read()
    start_file.close()
    return content

def parse_content(content):
    cases = content.split("-----")
    return cases

def prepare_content(cases):
    banks, entries, targetss, closes = [], [], [], []
    for case in cases:
        for line in case.split('\n'):
            if len(line) > 5:
                if line.startswith('Bank: '):
                    bank = line.replace('Bank: ', '')
                    bank = float(bank.partition('USD')[0])
                    banks.append(bank)
                elif line.startswith('Entry: '):
                    entry = line.replace('Entry: ', '')
                    entry = float(entry.partition('USD')[0])
                    entries.append(entry)
                elif line.startswith('Target: '):
                    targets = line.replace('Target: ', '').split('; ')
                    for i, t in enumerate(targets):
                        targets[i] = float(t.partition('USD')[0])
                    targetss.append(targets)
                elif line.startswith('Close: '):
                    close = line.replace('Close: ', '')
                    close = float(close.partition('USD')[0])
                    closes.append(close)
    return banks, entries, targetss, closes


def write_data(file_name, data):
    pass


def parse_data():
    pass


def main(file):
    content = read_data(file)
    cases = parse_content(content)
    banks, entries, targetss, closes = prepare_content(cases)
    write_data(md, result)


# content = read_data('deals.txt')
# result = content
# write_data('out.txt', result)


if __name__ == '__main__':
    main()