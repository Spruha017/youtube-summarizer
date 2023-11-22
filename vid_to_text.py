from youtube_transcript_api import YouTubeTranscriptApi as yta
import audio_to_text
import freq
# import pegasus_summarizer
# import nlp_summarizer
# import vid_id_extract
import streamlit as st

def vid_to_text(link,vid_id):

    # harman singh - manual script - https://youtu.be/Wn9iALMyS7c?si=q0LYZBrR9mSbj2b7 
    # --- https://www.youtube.com/watch?v=Wn9iALMyS7c

    # netflix death note dhruv rathee - no script allowed - https://www.youtube.com/watch?v=H3nzTmNlS4I&t=32s
    # power couple - auto-generated only - https://www.youtube.com/watch?v=6dpF_G3yMMQ
    # https://www.youtube.com/watch?v=1qbna6t1bzw 
    # what is  python - english - https://www.youtube.com/watch?v=Y8Tko2YC5hA
    #  fraz google - https://www.youtube.com/watch?v=ZSoTKpKGkCU

    # id = link.split('=')
    # vid_id = id[-1]
    
    # vid_id=vid_id_extract.video_id(link)
    # print(vid_id)
    # if vid_id==None:
    #     # print("invalid url")
    #     st.error("Invalid URL")


    # transcript_list = yta.list_transcripts(vid_id)
    # transcript = transcript_list.find_transcript(['de', 'en'])
    # print(
    # # a list of languages the transcript can be translated to
    # transcript.translation_languages,
    # )

    try:
        data = yta.get_transcript(vid_id)
        # print(data)
        return(clean_text(data))
    except:
        try:
            data = yta.get_transcript(vid_id, languages=['en-IN','hi','mr', 'en'])
            return(clean_text(data))
        except:
            # data = audio_to_text(link)
            data="hi"

        return(data)
    
    # return(data)

def clean_text(data):
    final_data = ''
    for val in data:
        for key,value in val.items():
            if key == 'text':
                final_data += ' ' + value
    # script=''
    # for x in data:
	#     t = x["text"]
	# 	if t != '[Music]':
	# 		script += t + " "

    # print(final_data)
    # process_data = final_data.splitlines()
    # clean_data = ''.join(process_data)
    # print(clean_data)
    text = open("transcript.txt",'w')
    text.write(final_data)
    text.close()

    summary_data=freq.main_freq()
    summary_text = open("summary.txt",'w')
    summary_text.write(summary_data)
    summary_text.close()

    # return(final_data)
    return(summary_data)