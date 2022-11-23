import pickle
from topicModel import TopicModel
from documentSummaries import DocumentSummaries

def getFederalDockets():
    dockets = ['APHIS-2006-0044']
    return dockets

def create_pickle():
    f = open("example_data/test1.txt", "r")
    outfile = open("example_data/test1.pickle",'wb')
    pickle.dump(f.readline(), outfile)
    outfile.close()

def getComments():
    regulations = dict()
    comments = list()
    dockets = getFederalDockets()
    for docket in dockets:
        file_name = 'example_data/' + docket + '.pickle'
        cmts = pickle.load(open(file_name, 'rb'))
        regulations[docket] = cmts
        comments.extend(cmts)
    return regulations, comments


def main(num_topics=15):
    
    # regulations, comments = getComments()
    f = open("example_data/test1.txt", "r")
    comments = [f.readline()]
    # print(len(comments))
    
    topicModel = TopicModel(num_topics)
    topicModel.fit(comments)

    # for docket_id, document in regulations.items():
    #     docSummaries = DocumentSummaries(topicModel, num_dominant_topics=3, number_of_sentences=4)
    #     docSummaries.summarize(document)
    #     print(docket_id)
    #     docSummaries.display()

    docSummaries = DocumentSummaries(topicModel, num_dominant_topics=3, number_of_sentences=1)
    docSummaries.summarize(comments[0])
    docSummaries.display()

main()
# create_pickle()