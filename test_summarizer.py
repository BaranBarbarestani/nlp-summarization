if __name__ == "__main__":
    text = """
    NASA's Artemis I mission is a test flight that will orbit the Moon, paving the way for future crewed missions. 
    The spacecraft, which includes the Space Launch System rocket and the Orion capsule, is being prepared for launch 
    in the coming months, with plans to send astronauts around the Moon by the mid-2020s.
    """

    from summarizer import TextSummarizer
    summarizer = TextSummarizer()
    print(summarizer.summarize(text))

