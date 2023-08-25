import random

import discord
import requests

from const import channel_name, display_name


class UtilsService:
    """
    discordボットを動かす際に仕様する共通部品クラス
    """

    def random_message_select(
        msg_list,
        channel_info: discord.VoiceState,
        member: discord.Member,
    ) -> str:
        """
        通知メッセージをランダムで生成します。

        Args:
            msg_list: メッセージ候補リスト
            channel_info: チャンネル情報
            member: ユーザー情報
        """
        # 通知メッセージテンプレートをランダムで選択
        msg_len = len(msg_list)
        ran_int = random.randint(0, msg_len - 1)

        # 通知メッセージテンプレートに引数を設定して返却
        message = (
            msg_list[ran_int]
            .replace(channel_name, channel_info.channel.name)
            .replace(display_name, member.display_name)
        )
        print(message)
        return message

    def get_global_ip_address_by_me():
        """
        このサーバーのIPアドレスを取得します。
        """
        res = requests.get("https://ifconfig.me")
        return res.text
