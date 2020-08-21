def generateStory(responses, story):
    storyString = ""
    for index, question in enumerate(story):
        if index < len(responses):
            if index != 0:
                responses[index] = responses[index].lower()
            storyString += question + responses[index]
        else: 
            if index != len(story) - 1:
                storyString += question
    return storyString