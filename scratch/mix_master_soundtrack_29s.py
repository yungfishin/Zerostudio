import subprocess
import pathlib
import sys

def build_master_audio():
    base_dir = pathlib.Path("Commercial_Projects_Archive").resolve()
    bgm_path = base_dir / "Project_Folders/YouTube Viral Script Data Miner/hyperframes/.claude/skills/changelog-video/assets/bgm.mp3"
    sfx_dir = base_dir / "tools/rea-capcut/public/builtin-assets"

    whoosh = sfx_dir / "sound-whoosh.wav"
    impact = sfx_dir / "sound-impact.wav"
    click = sfx_dir / "sound-click.wav"
    rise = sfx_dir / "sound-rise.wav"
    chime = sfx_dir / "sound-chime.wav"
    complete = sfx_dir / "sound-complete.wav"
    pop = sfx_dir / "sound-pop.wav"
    twinkle = sfx_dir / "sound-twinkle.wav"

    inputs = [
        "-i", str(bgm_path),    # 0
        "-i", str(whoosh),      # 1
        "-i", str(impact),      # 2
        "-i", str(click),       # 3
        "-i", str(rise),        # 4
        "-i", str(chime),       # 5
        "-i", str(complete),    # 6
        "-i", str(pop),         # 7
        "-i", str(twinkle)      # 8
    ]

    # Delays in milliseconds for 29s video:
    # Scene 1: 0.0s - 4.5s (Hook & Pain Points)
    # Scene 2: 4.5s - 10.0s (FREE Tier)
    # Scene 3: 10.0s - 17.5s (PRO Tier)
    # Scene 4: 17.5s - 24.0s (ULTRA Tier)
    # Scene 5: 24.0s - 29.0s (CTA & Comment Magnet)

    sfx_schedule = [
        # (input_index, delay_ms, volume, label)
        (1, 150, 0.70, "whoosh_intro"),
        (7, 800, 0.75, "pop_p1"),
        (7, 1600, 0.75, "pop_p2"),
        (7, 2400, 0.75, "pop_p3"),
        (4, 3200, 0.65, "rise_s1_climax"),
        (2, 3600, 0.85, "imp_s1"),
        # Scene 2 (FREE)
        (2, 4500, 1.10, "imp_free"),
        (3, 5300, 0.75, "c_free1"),
        (3, 6300, 0.75, "c_free2"),
        (3, 7300, 0.75, "c_free3"),
        (6, 8500, 0.90, "comp_free"),
        # Scene 3 (PRO)
        (4, 9300, 0.85, "rise_pro"),
        (2, 10000, 1.25, "imp_pro"),
        (3, 11000, 0.75, "c_pro1"),
        (3, 12200, 0.75, "c_pro2"),
        (7, 13500, 0.80, "pop_pro3"),
        (8, 14800, 0.85, "twinkle_pro4"),
        (1, 16000, 0.70, "whoosh_pro_end"),
        # Scene 4 (ULTRA)
        (4, 16800, 0.90, "rise_ultra"),
        (2, 17500, 1.30, "imp_ultra"),
        (3, 18600, 0.75, "c_ultra1"),
        (3, 19800, 0.75, "c_ultra2"),
        (7, 21000, 0.80, "pop_ultra3"),
        (6, 22200, 0.95, "comp_ultra4"),
        # Scene 5 (CTA Finale)
        (4, 23200, 0.95, "rise_cta"),
        (5, 24000, 1.20, "chime_cta"),
        (2, 24200, 1.00, "imp_cta"),
        (7, 25200, 0.90, "pop_comment"),
        (6, 26500, 1.05, "comp_founder"),
        (8, 27500, 0.85, "twinkle_end")
    ]

    filter_lines = []
    # BGM processing: 29s length, fade out from 26.5s to 29.0s
    filter_lines.append("[0:a]atrim=0:29,asetpts=PTS-STARTPTS,afade=t=out:st=26.5:d=2.5,volume=0.82[a_bgm];")

    amix_inputs = ["[a_bgm]"]
    for idx, (inp, delay, vol, lbl) in enumerate(sfx_schedule):
        filter_lines.append(f"[{inp}:a]adelay={delay}|{delay},volume={vol}[{lbl}];")
        amix_inputs.append(f"[{lbl}]")

    num_inputs = len(amix_inputs)
    amix_str = "".join(amix_inputs) + f"amix=inputs={num_inputs}:duration=first:dropout_transition=0,lowpass=f=8500,loudnorm=I=-14:TP=-1.0:LRA=7[out]"
    filter_lines.append(amix_str)

    filter_complex = "".join(filter_lines)

    out_wav = base_dir / "ZeroPDF_Studio/showcase_video/master_audio.wav"

    cmd = [
        "ffmpeg", "-y"
    ] + inputs + [
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-ar", "48000",
        "-t", "29",
        str(out_wav)
    ]

    print("Synthesizing 29s master soundtrack with FFmpeg...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Master soundtrack generated successfully: {out_wav} ({out_wav.stat().st_size} bytes)")
    else:
        print(f"FFmpeg Error:\n{res.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    build_master_audio()
