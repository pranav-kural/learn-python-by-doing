# to get arguments from command line
import sys
# import method to import data
from urllib.request import urlopen as uo


# fetch data and print words
def fetch_words(url):
    """
    Fetch a list of words from a URL
    
    Args:
        url: The URL of a UTF-8 text document
    
    Returns:
        story_words: A list of words
    """
    story = uo(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(story_words):
    for word in story_words:
        print(word)


# execute from shell
def main():
    # set url to the first arg provided over command line or default url value if no args
    url = sys.argv[1] if len(sys.argv) > 1 else 'http://sixty-north.com/c/t.txt'
    print_items(fetch_words(url))


# run main function is executed from shell
if __name__ == '__main__':
    main()
    
