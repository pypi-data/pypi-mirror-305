import os

from yuumi.requests import RequestHandler


class RealDebridAPI:
    """
    API wrapper for Real-Debrid.
    """
    BASE_URL = "https://api.real-debrid.com/rest/1.0"

    def __init__(self, access_token, rate_limit=None):
        self.access_token = access_token or os.getenv("RD_KEY", "")
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        self.request_handler = RequestHandler(self.BASE_URL, self.headers, rate_limit)

    def get_user_info(self):
        """
        Get the user info for the current user.
        """
        return self.request_handler.get("/user")

    def get_server_time(self):
        """
        Get the server time.
        """
        return self.request_handler.get("/time")

    def unrestrict_link(self, link):
        """
        Unrestrict a link.
        """
        data = {"link": link}
        return self.request_handler.post("/unrestrict/link", data)

    def disable_access_token(self):
        """
        Disable the access token.
        """
        return self.request_handler.get("/disable_access_token")

    def get_server_time_iso(self):
        """
        Get the server time in ISO format.
        """
        return self.request_handler.get("/time/iso")

    def check_link(self, link, password=None):
        """
        Check a link.
        """
        data = {"link": link}
        if password:
            data["password"] = password
        return self.request_handler.post("/unrestrict/check", data)

    def unrestrict_folder(self, link):
        """
        Unrestrict a folder.
        """
        data = {"link": link}
        return self.request_handler.post("/unrestrict/folder", data)

    def decrypt_container_file(self, file):
        """
        Decrypt a container file.
        """
        data = {"file": file}
        return self.request_handler.put("/unrestrict/containerFile", data)

    def get_downloads(self, offset=None, page=None, limit=100):
        """
        Get the downloads.
        """
        params = {}
        if offset:
            params["offset"] = offset
        if page:
            params["page"] = page
        params["limit"] = limit
        return self.request_handler.get("/downloads", params=params)

    def delete_download(self, download_id):
        """
        Delete a download.
        """
        return self.request_handler.delete(f"/downloads/delete/{download_id}")

    def get_supported_hosts(self):
        """
        Get the supported hosts.
        """
        return self.request_handler.get("/hosts")

    def get_host_status(self):
        """
        Get the host status.
        """
        return self.request_handler.get("/hosts/status")

    def get_host_regex(self):
        """
        Get the host regex.
        """
        return self.request_handler.get("/hosts/regex")

    def get_host_regex_folder(self):
        """
        Get the host regex folder.
        """
        return self.request_handler.get("/hosts/regexFolder")

    def get_host_domains(self):
        """
        Get the host domains.
        """
        return self.request_handler.get("/hosts/domains")

    def add_magnet(self, magnet_or_hash: str, host: str = None):
        """
        Add a magnet or infohash.

        :param magnet_or_hash: The magnet link or infohash.
        :param host: The host to add the torrent to.
        """
        if not magnet_or_hash.startswith("magnet:"):
            magnet_or_hash = f"magnet:?xt=urn:btih:{magnet_or_hash}"
        data = {"magnet": magnet_or_hash}
        if host:
            data["host"] = host
        return self.request_handler.post("/torrents/addMagnet", data)

    def select_torrent_files(self, torrent_id: str, files: list[int]):
        """
        Select torrent files.

        :param torrent_id: The ID of the torrent.
        :param files: A list of file indices to select.
        """
        payload = {"files": ",".join(map(str, files))}
        return self.request_handler.post(f"/torrents/selectFiles/{torrent_id}", payload)

    def select_playable_files(self, torrent_id: str, availability_data: dict[str, dict[int, dict[str, int]]]):
        """
        Select the playable files.

        :param torrent_id: The ID of the torrent.
        :param availability_data: The availability data from get_instant_availability.
        """
        video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".m4v", ".webm", ".mpg", ".mpeg", ".m2ts", ".ts"}
        playable_files = [
            file_index for file_index, file_info in availability_data.items()
            if "filename" in file_info and os.path.splitext(file_info["filename"])[1].lower() in video_extensions
        ]
        return self.select_torrent_files(torrent_id, playable_files)

    def delete_torrent(self, torrent_id):
        """
        Delete a torrent.
        """
        return self.request_handler.delete(f"/torrents/delete/{torrent_id}")

    def get_transcoding_links(self, file_id):
        """
        Get the transcoding links.
        """
        return self.request_handler.get(f"/streaming/transcode/{file_id}")

    def get_media_info(self, file_id):
        """
        Get the media info.
        """
        return self.request_handler.get(f"/streaming/mediaInfos/{file_id}")

    def get_user_settings(self):
        """
        Get the user settings.
        """
        return self.request_handler.get("/settings")

    def update_user_settings(self, setting_name, setting_value):
        """
        Update the user settings.
        """
        data = {"setting_name": setting_name, "setting_value": setting_value}
        return self.request_handler.post("/settings/update", data)

    def convert_fidelity_points(self):
        """
        Convert fidelity points.
        """
        return self.request_handler.post("/settings/convertPoints", {})

    def change_password(self):
        """
        Change the password.
        """
        return self.request_handler.post("/settings/changePassword", {})

    def upload_avatar(self, avatar_file):
        """
        Upload an avatar.
        """
        data = {"file": avatar_file}
        return self.request_handler.put("/settings/avatarFile", data)

    def get_torrents(self, offset=None, page=None, limit=100, filter=None):
        """
        Get the torrents.
        """
        params = {}
        if offset:
            params["offset"] = offset
        if page:
            params["page"] = page
        params["limit"] = limit
        if filter:
            params["filter"] = filter
        return self.request_handler.get("/torrents", params=params)

    def get_torrent_info(self, torrent_id):
        """
        Get the torrent info.
        """
        return self.request_handler.get(f"/torrents/info/{torrent_id}")

    def get_instant_availability(self, hashes: list[str]) -> dict[str, dict[int, dict[str, int]]]:
        """
        Get the instant availability of hash(es). Normalizes the output into a dict.

        Example:
            Input: "2f5a5ccb7dc32b7f7d7b150dd6efbce87d2fc371/10CE69DFFB064E887E8833E7754F71AA7532C997"
            Output:
            {
                "2f5a5ccb7dc32b7f7d7b150dd6efbce87d2fc371": {  # Cached
                    1: {
                        "filename": "Mortal.Kombat.2021.1080p.WEBRip.x264.AAC5.1-[YTS.MX].mp4",
                        "filesize": 2176618694
                    }
                },
                "10CE69DFFB064E887E8833E7754F71AA7532C997": {}, # Non-cached
            }
        """
        hashes_str = "/".join(hashes)
        data = self.request_handler.get(f"/torrents/instantAvailability/{hashes_str}")
        if not data:
            return {hash: {} for hash in hashes.split("/")}

        results = {}
        for hash, values in data.items():
            if "rd" in values and values["rd"]:
                result = {int(k): {"filename": v["filename"], "filesize": v["filesize"]} 
                          for container in values["rd"] for k, v in container.items()}
                results[hash] = result
            else:
                results[hash] = {}
        return results

    def get_active_torrent_count(self):
        """
        Get the active torrent count.
        """
        return self.request_handler.get("/torrents/activeCount")

    def get_available_hosts(self):
        """
        Get the available hosts.
        """
        return self.request_handler.get("/torrents/availableHosts")

    def add_torrent_file(self, torrent_file):
        """
        Add a torrent file.
        """
        data = {"file": torrent_file}
        return self.request_handler.put("/torrents/addTorrent", data)
