import json

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def ambil_usernames(data):
    usernames = set()
    for item in data:
        for user in item['string_list_data']:
            usernames.add(user['value'])
    return usernames

followers_1 = load_json('followers/followers_1.json')
following = load_json('followers/following.json')['relationships_following']

nama_pengikut = ambil_usernames(followers_1)
nama_yang_mengikuti = ambil_usernames(following)

tidak_mengikuti = nama_yang_mengikuti - nama_pengikut

if tidak_mengikuti:
    print(f"Ada {len(tidak_mengikuti)} akun yang tidak mengikuti kembali:")
    for username in tidak_mengikuti:
        print(f"- {username}")
else:
    print("Tidak ada akun yang tidak mengikuti anda kembali (semua mutual).")