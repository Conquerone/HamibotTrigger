import json
import sys

def main():
    hamibot_token = sys.argv[1]
    hamibot_paras = json.loads(sys.argv[2])
    workflow_name = sys.argv[3]
    wechat_uid = sys.argv[4]

    # Debug prints
    print(f"HAMIBOT_TOKEN: {hamibot_token}")
    print(f"HAMIBOT_PARAS: {hamibot_paras}")
    print(f"WORKFLOW_NAME: {workflow_name}")
    print(f"WECHAT_UID: {wechat_uid}")

if __name__ == "__main__":
    main()import json
import sys

def main():
    hamibot_token = sys.argv[1]
    hamibot_paras = json.loads(sys.argv[2])
    workflow_name = sys.argv[3]
    wechat_uid = sys.argv[4]

    # Debug prints
    print(f"HAMIBOT_TOKEN: {hamibot_token}")
    print(f"HAMIBOT_PARAS: {hamibot_paras}")
    print(f"WORKFLOW_NAME: {workflow_name}")
    print(f"WECHAT_UID: {wechat_uid}")

if __name__ == "__main__":
    main()
