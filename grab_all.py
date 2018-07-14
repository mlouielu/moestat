import csv
import moestat


def download_csv_with_all_parameters(title, qno):
    ql = moestat.get_search_parameters(qno)
    result = moestat.get_search_result(qno, ql)
    with open(f'dataset/{title.replace("/", ",")}.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',', quotechar='"')
        for r in result:
            w.writerow(r)


# Fetching 高級中等學校專業群(職業)科學生及畢業生數-依學科類別查詢 to CSV file
# download_csv_with_all_parameters('高級中等學校專業群(職業)科學生及畢業生數-依學科類別查詢', 'MQAyADQA0')


# Fetching all data and save as csv
print('[*] Get all qno in stats.moe.gov.tw')
qnos = moestat.search.get_all_qno()

print('[*] Start to get all data')
for title, qno in qnos:
    if isinstance(qno, list):
        # We got multiple qno in one category
        print(f'[-] Found multiple data in one set: {title}')
        for by, q in qno:
            print(f'    [*] Downloading: {title}-{by}')
            download_csv_with_all_parameters(f'{title}-{by}', q)
    else:
        print(f'[*] Downloading: {title}')
        download_csv_with_all_parameters(title, qno)
