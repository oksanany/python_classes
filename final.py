class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return self.targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        percent_targets = []
        for t in self.targets:
            per_t = round(100*t/self.entry - 1, 3)
            percent_targets.append(per_t)
        return percent_targets



    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        percent_targets = self.get_target_percents()
        banks = []
        for t in percent_targets:
            banks.append(round(self.bank*(1 + t/100), 3))
        return banks

    def formatted_content(self):
        target_percents = self.get_target_percents()
        target_banks = self.get_target_banks()
        # текстовое представление сделки
        ans = "BANK: {}\nSTART_PRICE: {}\nSTOP_PRICE: {}\n\n".format(self.bank, self.entry, self.close)
        for i, t in enumerate(target_percents):
            ans = ans + "{} target: {}\nPercent: {}%\nBank: {}\n\n".format(i+1, self.targets[i], t, target_banks[i])
        return ans


def read_data(file_name):
    start_file = open(file_name, encoding='utf-8')
    content = start_file.read()
    start_file.close()
    return content

def parse_content(content):
    cases = content.split("-----")
    return cases

def prepare_content(case):
    bank, entry, targets, close = [], [], [], []
    for line in case.split('\n'):
        line = line.strip()
        if line.startswith('Bank: '):
            bank = line.replace('Bank: ', '')
            bank = float(bank.partition('USD')[0])
        elif line.startswith('Entry: '):
            entry = line.replace('Entry: ', '')
            entry = float(entry.partition('USD')[0])
        elif line.startswith('Target: '):
            targets = line.replace('Target: ', '').split('; ')
            for i, t in enumerate(targets):
                targets[i] = float(t.partition('USD')[0])
        elif line.startswith('Close: '):
            close = line.replace('Close: ', '')
            close = float(close.partition('USD')[0])
    return bank, entry, targets, close


def write_data(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    file.write(data)
    file.close()




def main(file):
    content = read_data(file)
    cases = parse_content(content)
    ans = []
    for case in cases:
        case = case.strip()
        if len(case) > 0:
            bank, entry, targets, close = prepare_content(case)
            strategy_deal = StrategyDeal(bank, entry, targets, close)
            ans.append(strategy_deal.formatted_content())
    result = "\n-----\n\n".join(ans)
    write_data('output.txt', result)


if __name__ == '__main__':
    main('input.txt')




# content = read_data('deals.txt')
# result = content
# write_data('out.txt', result)


#if __name__ == '__main__':
 #   main()
