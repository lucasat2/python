import re

def parse_log_line(line):
    pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) '  # IP
        r'\[(?P<timestamp>.+?)\] '  # Timestamp
        r'"(?P<method>\w+) (?P<path>[^ ]+) HTTP/\d\.\d" '  # Método e URL
        r'(?P<status>\d+) '  # Código de status
        r'(?P<size>\d+) '  # Tamanho da resposta
        r'"(?P<user_agent>.+?)" '  # User Agent
        r'(?P<response_time>[\d\.]+)s'  # Tempo de resposta
    )
    
    match = pattern.match(line)
    if match:
        data = match.groupdict()
        data['status'] = int(data['status'])
        data['size'] = int(data['size'])
        data['response_time'] = float(data['response_time'])
        return data
    else:
        return None

def parse_log_file(file_path):
    log_entries = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            entry = parse_log_line(line.strip())
            if entry:
                log_entries.append(entry)
    return log_entries

# Exemplo de uso
if __name__ == "__main__":
    log_entries = parse_log_file("server_access.log")
    for entry in log_entries:
        print(entry)
