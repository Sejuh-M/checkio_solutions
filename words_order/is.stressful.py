def is_stressful(subj):
    subj = str(subj.lower())
    try:
        if subj[subj.index('h'):].index('h') < (subj[subj.index('h'):].index('e')):
            if (subj[subj.index('h'):].index('e')) < (subj[subj.index('h'):].index('l')):
                if subj[subj.index('h'):].index('l') < subj[subj.index('h'):].index('p'):
                    return (True)
        else:
            return False

    except:
        try:
            if subj[subj.index('a'):].index('a') < (subj[subj.index('a'):].index('s')):
                if (subj[subj.index('s'):].index('s')) < (subj[subj.index('s'):].index('a')):
                    if subj[subj.index('s'):].index('a') < subj[subj.index('s'):].index('p'):
                        return True
            else:
                return False
        except:
            return False
if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')