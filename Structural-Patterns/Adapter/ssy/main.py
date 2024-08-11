class MediaPlayer:
    """
    The MediaPlayer defines the standard interface for playing audio files.
    """

    def play(self, audio_type: str, file_name: str) -> None:
        raise NotImplementedError("This method should be overridden.")


class AdvancedMediaPlayer:
    """
    The AdvancedMediaPlayer defines an interface for playing advanced media formats.
    """

    def play_mp4(self, file_name: str) -> None:
        raise NotImplementedError("This method should be overridden.")

    def play_vlc(self, file_name: str) -> None:
        raise NotImplementedError("This method should be overridden.")


class Mp4Player(AdvancedMediaPlayer):
    """
    Mp4Player is a concrete implementation of AdvancedMediaPlayer for playing MP4 files.
    """

    def play_mp4(self, file_name: str) -> None:
        print(f"Playing mp4 file: {file_name}")

    def play_vlc(self, file_name: str) -> None:
        pass


class VlcPlayer(AdvancedMediaPlayer):
    """
    VlcPlayer is a concrete implementation of AdvancedMediaPlayer for playing VLC files.
    """

    def play_mp4(self, file_name: str) -> None:
        pass

    def play_vlc(self, file_name: str) -> None:
        print(f"Playing vlc file: {file_name}")


class MediaAdapter(MediaPlayer):
    """
    MediaAdapter bridges the interface between MediaPlayer and AdvancedMediaPlayer.
    """

    def __init__(self, audio_type: str) -> None:
        self.advanced_media_player = None

        if audio_type == "mp4":
            self.advanced_media_player = Mp4Player()
        elif audio_type == "vlc":
            self.advanced_media_player = VlcPlayer()

    def play(self, audio_type: str, file_name: str) -> None:
        if audio_type == "mp4":
            self.advanced_media_player.play_mp4(file_name)
        elif audio_type == "vlc":
            self.advanced_media_player.play_vlc(file_name)


class AudioPlayer(MediaPlayer):
    """
    AudioPlayer is a concrete implementation of MediaPlayer for playing standard audio files.
    """

    def play(self, audio_type: str, file_name: str) -> None:
        if audio_type == "mp3":
            print(f"Playing mp3 file: {file_name}")
        elif audio_type in ("mp4", "vlc"):
            # Use MediaAdapter for unsupported formats
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, file_name)
        else:
            print(f"Invalid media format: {audio_type}")


if __name__ == "__main__":
    audio_player = AudioPlayer()

    audio_player.play("mp3", "song.mp3")
    audio_player.play("mp4", "video.mp4")
    audio_player.play("vlc", "movie.vlc")
    audio_player.play("avi", "animation.avi")
