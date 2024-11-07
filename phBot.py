from typing import Dict, overload, Literal, List, Tuple

# Client
class Client(Dict):
    @overload
    def __getitem__(self, key: Literal['path']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['window', 'pid']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['running']) -> bool: pass


def get_client() -> None | Client: pass

# Guild
class Guild(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'master']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['count', 'level']) -> int: pass

def get_guild_union() -> None | dict[int, Guild]: pass

class GuildMember(Dict):
    @overload
    def __getitem__(self, key: Literal['name']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'level', 'region', 'donated_gp', 'online', 'authority']) -> int: pass

def get_guild() -> None | dict[int, GuildMember]: pass

# Players
class Item(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'quantity', 'plus', 'durability']) -> int: pass

class Player(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'guild', 'grant']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y']) -> float: pass

    @overload
    def __getitem__(self, key: Literal['dead']) -> bool: pass

    @overload
    def __getitem__(self, key: Literal['items']) -> List[Item]: pass

def get_players() -> None | dict[int, Player]: pass

# Party
class PartyMember(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'guild']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['level', 'player_id', 'model', 'hp_percent', 'mp_percent', 'region']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y', 'angle']) -> float: pass

    @overload
    def __getitem__(self, key: Literal['leader']) -> bool: pass

def get_party() -> None | dict[int, PartyMember]: pass

# NPC
class Npc(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'region']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y']) -> float: pass

def get_npcs() -> None | dict[int, Npc]: pass

class NpcItem(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'data']) -> int: pass

def get_npc_goods(model: int) -> dict[int, dict[int, NpcItem]]: pass

# Character
class Character(Dict):
    @overload
    def __getitem__(self, key: Literal['server', 'name', 'guild', 'job_name', 'zone_name', 'job_type']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'region', 'hp', 'mp', 'hp_max', 'mp_max', 'level', 'gold', 'current_exp', 'max_exp', 'sp', 'job_current_exp', 'job_max_exp', 'player_id', 'account_id', 'locale', 'death_count', 'drop_count', 'rare_drop_count', 'job_level', 'gold_per_loop', 'kill_count', 'time_to_level']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y', 'exp_ratio', 'exp_minute', 'exp_hour', 'sp_minute', 'sp_hour', 'exp_gained', 'sp_gained']) -> float: pass

    @overload
    def __getitem__(self, key: Literal['dead', 'botting', 'tracing', 'trading', 'manager']) -> bool: pass

def get_character_data() -> None | Character: pass

class Position(Dict):
    @overload
    def __getitem__(self, key: Literal['region']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y', 'z']) -> float: pass

def get_position() -> None | Position: pass

class ActiveSkill(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

def get_active_skills() -> None | dict[int, ActiveSkill]: pass

class Skill(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['level', 'mastery', 'cast_time', 'cooldown', 'duration']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['active', 'can_cast']) -> bool: pass

def get_skills() -> None | dict[int, Skill]: pass

class Mastery(Dict):
    @overload
    def __getitem__(self, key: Literal['name']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['level', 'sp']) -> int: pass

def get_mastery() -> None | dict[int, Mastery]: pass

# Academy
class AcademyInfo(Dict):
    @overload
    def __getitem__(self, key: Literal['name']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['online', 'type', 'level']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y']) -> float: pass

class Academy(Dict):
    @overload
    def __getitem__(self, key: Literal['id']) -> int: pass

    @overload
    def __getitem__(self, key: int) -> AcademyInfo: pass

def get_academy() -> None | Academy: pass

# Inventory
class Inventory(Dict):
    @overload
    def __getitem__(self, key: Literal['size, gold']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['items']) -> List[Item]: pass

def get_inventory() -> None | Inventory: pass
def get_storage() -> None | Inventory: pass
def get_guild_storage() -> None | Inventory: pass
def get_job_pouch() -> None | Inventory: pass
def sort_inventory() -> bool: pass
def use_return_scroll() -> bool: pass
def reverse_return(t: int, name: str) -> bool: pass

# Pets
class Pet(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'remaining', 'hp']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['mounted']) -> bool: pass

    @overload
    def __getitem__(self, key: Literal['type']) -> Literal['none', 'fellow', 'horse', 'pick', 'transport', 'wolf']: pass

    @overload
    def __getitem__(self, key: Literal['items']) -> List[Item]: pass

def get_pets() -> None | dict[int, Pet]: pass

# Monsters
class Monster(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'type', 'region', 'hp', 'max_hp', 'attacking']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y']) -> float: pass

def get_monsters() -> None | dict[int, Monster]: pass

# Encoding
def get_encoding() -> None | Literal['utf-16le', 'cp1251', 'gb18030', 'cp1251', 'big5', 'sjis', 'euc-kr']: pass

# Locale
def get_locale() -> int: pass

# Config
def get_config_path() -> str | None: pass
def get_config_dir() -> str: pass
def get_log_dir() -> str: pass

# Botting
def start_bot() -> bool: pass
def stop_bot() -> bool: pass
def start_trace(name: str) -> bool: pass
def stop_trace() -> bool: pass
def start_trade() -> bool: pass
def stop_trade() -> bool: pass

# Taxi
class TaxiMember(Dict):
    @overload
    def __getitem__(self, key: Literal['remaining', 'party_id', 'player_id', 'level']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y']) -> float: pass

    @overload
    def __getitem__(self, key: Literal['exchanging', 'dead', 'party']) -> bool: pass


def get_taxi() -> None | TaxiMember: pass

# Packet Injection
def inject_joymax(opcode: int, data: bytes, encrypted: bool) -> None: pass
def inject_silkroad(opcode: int, data: bytes, encrypted: bool) -> None: pass

# Log
def log(text: str) -> None: pass

# Game Data
class ItemData(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['max_stack', 'level', 'tid1', 'tid2', 'tid3']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['cash_item', 'rare']) -> bool: pass

def get_item(id: int) -> None | ItemData: pass
def get_item_string(servername: str) -> None | ItemData: pass

class MonsterData(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['level', 'hp']) -> int: pass

def get_monster(id: int) -> None | MonsterData: pass
def get_monster_string(servername: str) -> None | MonsterData: pass

class SkillData(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['level', 'mastery', 'cast_time', 'cool_down', 'duration', 'sp', 'mp']) -> int: pass

def get_skill(id: int) -> None | SkillData: pass
def get_zone_name(region: int) -> None | str: pass

# Teleport
def get_teleport_data(tp1: str, tp2: str) -> None | Tuple[int, int]: pass

# Training Area
def set_training_position(region: int, x: float, y: float, z: float) -> bool: pass
def set_training_script(path: str) -> None | bool: pass
def set_training_radius(radius: float) -> bool: pass

class TrainingArea(Dict):
    @overload
    def __getitem__(self, key: Literal['path']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['region']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y', 'z', 'radius', 'pick_radius']) -> float: pass

def get_training_area() -> None | TrainingArea: pass
def set_training_area(name: str) -> bool: pass

# Command Line Arguments
def get_command_line_args() -> None | List[str]: pass

# Movement
def move_to(x: float, y: float, z: float) -> None: pass
def move_to_region(region: int, x: float, y: float, z: float) -> None: pass

# Quests
class QuestObjective(Dict):
    @overload
    def __getitem__(self, key: Literal['servername', 'notice']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['id', 'progress']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['completed']) -> bool: pass

class Quest(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['type']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['npc']) -> List[int]: pass

    @overload
    def __getitem__(self, key: Literal['completed', 'objectives_completed']) -> bool: pass

    @overload
    def __getitem__(self, key: Literal['objectives']) -> List[QuestObjective]: pass

def get_quests() -> None | dict[int, Quest]: pass

# Drops
class Drop(Dict):
    @overload
    def __getitem__(self, key: Literal['name', 'servername']) -> str: pass

    @overload
    def __getitem__(self, key: Literal['model', 'region', 'plus']) -> int: pass

    @overload
    def __getitem__(self, key: Literal['x', 'y', 'z']) -> float: pass

    @overload
    def __getitem__(self, key: Literal['can_pick', 'blue']) -> bool: pass

def get_drops() -> None | dict[int, Drop]: pass

# Paths
def generate_path(x: float, y: float) -> None | Literal[False] | List[Tuple[float, float]]: pass
def generate_script(region: int, x: float, y: float, z: float) -> None | Literal[False] | List[str]: pass

# Script
def start_script(script: str) -> None: pass
def stop_script() -> None: pass

# Notifications
def create_notification(text: str) -> bool: pass
def create_notification_item(text: str, id: int) -> bool: pass

# Alchemy
def start_alchemy() -> bool: pass
def stop_alchemy() -> bool: pass
def reset_alchemy() -> bool: pass
def add_alchemy(item: dict[Literal['type', 'slot', 'stop', 'success', 'failure', 'powder', 'astral', 'steady', 'immortal', 'lucky', 'stop_attempt', 'stop_destroyed', 'skip_fail'], str | int]) -> bool: pass

# Misc
def get_version() -> str: pass
def select_character() -> None: pass
def set_profile(name: str) -> bool: pass
def get_profile() -> None | str: pass
def disconnect() -> None: pass
def show_notification(title: str, msg: str) -> bool: pass
def play_wav(path: str) -> None: pass
def minimize() -> None: pass
def unminimize() -> None: pass