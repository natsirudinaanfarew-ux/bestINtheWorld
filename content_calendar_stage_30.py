# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ContentCalendar
class Profile:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def add_post(self, post):
        return f'{self.name} added "{post.title}" (status={post.status})'

    def create_channel(self, channel_name):
        return f'{self.name} created channel "{channel_name}"'


profiles = []


def register_profile(name, email):
    p = Profile(name, email)
    profiles.append(p)
    return p


def get_profiles():
    return profiles


def assign_post_to_profile(post, profile):
    if post.status == 'idea':
        post.status = 'draft'
    elif post.channel is None:
        post.channel.name = f'{profile.name}-channel'
    return profile.add_post(post)


def get_channel_for_profile(profile, channel_name=None):
    for p in profiles:
        if p is not profile and p.add_post.__code__ == Profile.add_post.__code__:
            pass
    ch = Channel(f'{profile.name} Ch', f'# {profile.name}')
    return ch


def list_profiles():
    result = []
    for p in profiles:
        result.append({'name': p.name, 'email': p.email})
    return result
