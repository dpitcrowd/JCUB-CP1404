import wikipedia

title = input('Enter your request --> ')

while title != '':
    try:
        my_search = wikipedia.page(title)
        #print(wikipedia.search(title))
        # wikipedia.page enables you to load and access data from full Wikipedia pages.
        #print('\n', wikipedia.page(title))
        print(my_search.title)
        # To get the summary of an article
        #print('\n', wikipedia.summary(title))
        print(my_search.content)
        # U.R.L.
        #print('\n', wikipedia.url(title))
        print(my_search.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError:
        print('Your request does not match any pages. Try another query!')

    title = input('Enter your request --> ')