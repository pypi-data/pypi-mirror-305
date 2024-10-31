# from googletrans import Translator
import requests
import pysrt
import os
import sys
import shutil
import ffmpeg

def extract_subtitles(video_file, output_srt, track_number = 1):
    # Extract subtitles using FFmpeg
    try:
        (
            ffmpeg
            .input(video_file)
            .output(output_srt, map='s:' + str(track_number - 1))
            .run()
        )
        print(f'Subtitles extracted from {video_file} and saved to {output_srt}')
    except ffmpeg.Error as e:
        print(f'Error: {e}')


def split_list(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]


def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def multi_find(source_text, search_key):
    return [pos for pos in range(len(source_text)) if source_text.startswith(search_key, pos)]


def translate_text(text, source_lang='en', target_lang='zh-CN'):
    url = 'https://translate.google.com/translate_a/single'
    params = {
        'client': 'gtx',
        'sl': source_lang,
        'tl': target_lang,
        'dt': 't',
        'q': text,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        result = response.json()
        extracted_result = [raw_line[0] for raw_line in result[0]]
        return extracted_result
    else:
        return None


# def translate_lines(translator, lines, source_language, target_language):
def translate_lines(lines, source_language, target_language):
    # lines = [line + '\n' for line in lines]
    # source_text = "@@@".join(lines)
    source_text = "\n".join(lines)
    # translation = translator.translate(source_text, src=source_language, dest=target_language)
    # translated_lines = translation.text.split("@@@")
    # translated_lines = translation.split("@@@")
    # translated_lines = [line.replace("@ @@", "@@@").replace("@@ @", "@@@").split("@@@") for line in translated_lines]
    translated_lines = translate_text(source_text, source_lang=source_language, target_lang=target_language)
    # translated_lines = flatten_list(translated_lines)
    return translated_lines


def combine_lines(translated_lines):
    result = []
    temp_line = ""
    for raw_line in translated_lines:
        if str(raw_line).endswith("\n"):
            result.append(raw_line)
            temp_line = ""
        else:
            temp_line += raw_line
            continue
    result.append(translated_lines[-1])
    return result


def translate_srt(input_file, output_file, source_language, target_language):
    result = True

    # Load SRT file
    srt_file = pysrt.open(input_file, encoding='utf-8')
    
    lines = [sub.text for sub in srt_file]
    # split all lines into small list of lines(no more than 200 lines in each sub list)
    sub_lines_list = split_list(lines, 200)

    # Initialize translator
    # translator = Translator()

    translated_lines_list = []
    # Loop each each small list of lines, translate them.
    for sub_lines in sub_lines_list:
        # translated_lines = translate_lines(translator, sub_lines, source_language, target_language)
        translated_lines = translate_lines(sub_lines, source_language, target_language)
        if len(translated_lines) == len(sub_lines):
            translated_lines_list.append(translated_lines)
        else:
            # translated_lines = [[sub_line + "\n" for sub_line in (line[:-1].split("\n"))] if len(multi_find(line, "\n")) > 1 else [line] for line in translated_lines]
            # translated_lines = flatten_list(translated_lines)
            translated_lines = combine_lines(translated_lines)
            if len(translated_lines) == len(sub_lines):
                translated_lines_list.append(translated_lines)
            else:
                print("Can not translate the subtitle correctly.")
                result = False
                break
    
    if not result:
        return result

    translated_lines = flatten_list(translated_lines_list)
    # Translate each subtitle
    for sub, translated_line in zip(srt_file, translated_lines):
        # Merge the source subtitle and the translated subtitle.
        sub.text = "<font color='#ffff54'>" + sub.text + "</font>" + "\n" + translated_line

    # Save translated SRT file
    srt_file.save(output_file, encoding='utf-8')

    return result


def print_usage():
    print("""
        Usage: srt_trans test_file.srt [-src_lang en -dest_lang zh-CN -proxy http://youdomain:your_port]
        Example:
            srt_trans ./test_video.mkv
            srt_trans ./test_video.mkv -src_lang en -dest_lang zh-TW
            srt_trans ./test_video.mkv -src_lang en -dest_lang zh-CN -proxy http://127.0.0.1:8118
            srt_trans ./test_video.mkv -track_number 2
            srt_trans ./test_video.mkv -src_lang en -dest_lang zh-TW -track_number 2
            srt_trans ./test_video.mkv -src_lang en -dest_lang zh-CN -proxy http://127.0.0.1:8118 -track_number 2
            srt_trans test_file.srt
            srt_trans test_file.srt -src_lang en -dest_lang zh-TW
            srt_trans test_file.srt -src_lang en -dest_lang ja
            srt_trans test_file.srt -src_lang en -dest_lang zh-CN
            srt_trans test_file.srt -src_lang en -dest_lang fr -proxy http://127.0.0.1:8118
    """)


def pre_process_srt_file(input_file):
    # Load SRT file
    srt_file = pysrt.open(input_file, encoding='utf-8')
    for sub in srt_file:
        sub.text = str(sub.text).replace("\n", " ").replace("<i>", "").replace("</i>", "").replace("{\\an8}", "").replace("\"", "")
    srt_file.save(input_file, encoding='utf-8')


def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"{input_file} not exists!")
        return
    
    source_language = "en"      # Source language code (e.g., "en" for English)
    target_language = "zh-CN"   # Target language code (e.g., "zh-CN" for Simple Chinese)
    
    if str(input_file).lower().endswith(".mkv"):
        track_number = 1
        video_file = ""
        if len(sys.argv) == 2:
            pass
        elif len(sys.argv) == 4 and sys.argv[2] == "-track_number":
            track_number = sys.argv[3]
        elif len(sys.argv) == 6 and sys.argv[2] == "-src_lang" and sys.argv[4] == "-dest_lang":
            source_language = sys.argv[3]
            target_language = sys.argv[5]
        elif len(sys.argv) == 8 and sys.argv[2] == "-src_lang" and sys.argv[4] == "-dest_lang" and sys.argv[6] == "-track_number":
            source_language = sys.argv[3]
            target_language = sys.argv[5]
            track_number = sys.argv[7]
        elif len(sys.argv) == 8 and sys.argv[2] == "-src_lang" and sys.argv[4] == "-dest_lang" and sys.argv[6] == "-proxy":
            source_language = sys.argv[3]
            target_language = sys.argv[5]
            proxy = sys.argv[7]
            # Set environment variables (For example: "http://127.0.0.1:8118")
            os.environ['http_proxy'] = proxy
            os.environ['https_proxy'] = proxy
        elif len(sys.argv) == 10 and sys.argv[2] == "-src_lang"  and sys.argv[4] == "-dest_lang"and sys.argv[6] == "-proxy" and sys.argv[8] == "-track_number":
            source_language = sys.argv[3]
            target_language = sys.argv[5]
            proxy = sys.argv[7]
            track_number = sys.argv[9]
            # Set environment variables (For example: "http://127.0.0.1:8118")
            os.environ['http_proxy'] = proxy
            os.environ['https_proxy'] = proxy
        else:
            print("Invalid arguments!")
            return
        if not str(track_number).isdigit():
            print("Invalid track_number, it should be an int!")
            return

        video_file = input_file
        input_file = video_file.replace(".mkv", ".srt")
        extract_subtitles(video_file, input_file, int(track_number))
    else:
        if len(sys.argv) == 2:
            pass
        elif len(sys.argv) == 6 and sys.argv[2] == "-src_lang" and sys.argv[4] == "-dest_lang":
            source_language = sys.argv[3]
            target_language = sys.argv[5]
        elif len(sys.argv) == 8 and sys.argv[2] == "-src_lang" and sys.argv[4] == "-dest_lang" and sys.argv[6] == "-proxy":
            source_language = sys.argv[3]
            target_language = sys.argv[5]
            proxy = sys.argv[7]
            # Set environment variables (For example: "http://127.0.0.1:8118")
            os.environ['http_proxy'] = proxy
            os.environ['https_proxy'] = proxy
        else:
            print("Invalid arguments!")
            return
    
    pre_process_srt_file(input_file)

    output_file = str(input_file).replace(".srt", f".{target_language}.srt")
    translate_result = translate_srt(input_file, output_file, source_language, target_language)
    if not translate_result:
        return
    
    os.remove(input_file)
    shutil.move(output_file, input_file)


if __name__ == "__main__":
    main()