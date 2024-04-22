import time
import collections


# Function to read log file and count occurrences of keywords
def count_keywords(log_file, keywords):
    keyword_counts = {keyword: 0 for keyword in keywords}

    with open(log_file, 'r') as file:
        for line in file:
            for keyword in keywords:
                if keyword in line:
                    keyword_counts[keyword] += 1

    return keyword_counts


# Function to generate report of top keyword occurrences
def generate_report(keyword_counts, top_n=5):
    sorted_counts = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

    report = "Top {} Keyword Occurrences:\n".format(top_n)
    for keyword, count in sorted_counts[:top_n]:
        report += f"{keyword}: {count}\n"

    return report


# Main function to continuously monitor log file
def monitor_log(log_file, keywords, interval=10, top_n=5):
    while True:
        keyword_counts = count_keywords(log_file, keywords)
        report = generate_report(keyword_counts, top_n)
        print(report)
        time.sleep(interval)


if __name__ == "_main_":
    log_file = "path/to/your/logfile.log"
    keywords = ["error", "warning", "exception"]  # Specify keywords to monitor
    monitor_log(log_file, keywords)