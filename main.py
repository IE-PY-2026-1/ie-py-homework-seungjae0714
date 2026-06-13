# 파일이름 :여행도우미 트래버
# 작 성 자 :강승재


import random
import time

print(f"{'='*50}")
print(f" ✈️ 스마트 여행도우미 [트래버] 시스템 가동 ✈️ ")
print(f"{'='*50}\n")

# ==========================================
# [1단계] 초기 사용자 정보 설정
# ==========================================
user_name = input("여행자님의 성함을 입력해주세요: ")
travel_destination = input("가고 싶은 여행지를 입력해주세요 (예: 일본, 미국, 유럽 등): ")
total_search_count = 0

# ==========================================
# [2단계] 환율 및 항공권 감시
# ==========================================
for main_loop in range(10):
    print(f"\n{'-'*50}")
   
    target_exchange = float(input(f"[{travel_destination}] 목표 환율을 입력하세요 (예: 900.0): "))
    target_flight = int(input(f"[{travel_destination}] 목표 항공권 가격을 입력하세요 (원): "))
       
    print("\n🔎 실시간 환율 및 항공권 가격을 조회합니다...")
    time.sleep(1)
   
    is_success = False 
   
    for trial in range(1, 4):
        total_search_count += 1
       
        if "일본" in travel_destination:
            base_rate = 920.0
            base_flight = 300000
        elif "미국" in travel_destination:
            base_rate = 1400.0
            base_flight = 1500000
        elif "유럽" in travel_destination:
            base_rate = 1650.0
            base_flight = 1700000
        else:
            base_rate = 1000.0
            base_flight = 500000
           
        current_exchange = base_rate + random.uniform(-30, 30)
        current_flight = base_flight + random.randint(-50000, 50000)
       
        print(f" > [{trial}차 시도] 환율: {current_exchange:.2f}원 / 항공권: {current_flight:,}원")
       
        if current_exchange <= target_exchange and current_flight <= target_flight:
            print(f"\n🎊 성공! 환율과 항공권 모두 목표가 이하로 떨어졌습니다!")
            is_success = True
            break 
        else:
            time.sleep(0.5)
           
    if is_success:
        break 
    else:
        print(f"\n⚠️ 3회 확인 결과, 아직 시장가가 높습니다. 목표가를 다시 설정해 주세요.")

# ==========================================
# [3단계] 스마트 짐 검사 시스템
# ==========================================
packing_list = []
print(f"\n{'='*50}")
print(f" 🧳 [짐 검사] {user_name}님의 캐리어 검사를 시작합니다.")
print(f" (짐을 하나씩 입력하세요. 다 쌌다면 '끝'을 입력하세요.)")
print(f"{'='*50}")

for i in range(20):
    item = input(" > 가방에 넣은 물건 (그만하려면 '끝' 입력): ")
    if item == "끝":
        print("\n🔎 입력을 완료했습니다. 필수품 누락 여부를 확인합니다...")
        time.sleep(1)
        break
    if item != "":
        packing_list.append(item)

if "여권" not in packing_list:
    print(f"🚨 [경고] 가장 중요한 '여권'이 빠져있습니다! (자동 추가 완료)")
    packing_list.insert(0, "여권")
else:
    print("✅ 필수 확인: '여권'이 안전하게 들어있습니다.")

packing_list.sort()
total_items = len(packing_list)
print(f"🎒 총 {total_items}개의 짐이 준비되었습니다: {packing_list}")

# ==========================================
# [4단계] 수하물 보안 및 무게 검사
# ==========================================
print(f"\n{'='*50}")
print(f" 🛃 [보안/무게 검사] 수하물 규정 체크")
print(f"{'='*50}")

input_success = False  # 💡 입력을 성공했는지 체크하는 변수

for attempt in range(5):
    baggage_type = input("짐을 기내에 들고 타시나요, 위탁으로 보내시나요? (기내 / 위탁): ")
   
    if baggage_type in ["기내", "위탁"]:
        input_success = True  # 성공적으로 입력함
        break
   
    if attempt < 4:
        print(f"⚠️ '기내' 또는 '위탁'으로 정확히 입력해주세요. (남은 횟수: {4 - attempt}번)")


if input_success:
    # 수하물 종류별 검사
    if baggage_type == "기내":
        if ("칼" in str(packing_list)) or ("가위" in str(packing_list)):
             print(f"🚨 [주의] 리스트에 날카로운 물건이 있습니다. 기내 반입이 불가합니다.")
        liquid_check = input("가방 안에 100ml 이상의 액체가 있습니까? (예/아니오): ")
        if liquid_check == "예":
            print("❌ [경고] 100ml 이상 액체는 기내 반입 금지! 위탁으로 보내세요.")

    elif baggage_type == "위탁":
        if ("보조배터리" in str(packing_list)) or ("라이터" in str(packing_list)):
            print(f"🚨 [주의] 화재 위험 물품(배터리, 라이터)은 화물칸 탑재 불가입니다.")
            print(" -> 해당 물품은 빼서 기내에 들고 타세요.")

    carry_on_weight = float(input("\n1. 기내 짐 총 무게(kg): "))
    checked_weight = float(input("2. 위탁 수하물 총 무게(kg): "))

    is_over_limit = False

    if carry_on_weight > 7:
        print(f"⚠️ 기내 짐({carry_on_weight}kg)이 기준(7kg)을 초과했습니다.")
        is_over_limit = True
    if checked_weight > 15:
        print(f"⚠️ 위탁 수하물({checked_weight}kg)이 기준(15kg)을 초과했습니다. 추가 비용 주의!")
        is_over_limit = True

    if not is_over_limit:
        print(f"\n✨ 무게가 아주 넉넉합니다! {travel_destination} 여행 시 필요한 상비약, 혹은 자신만의 개성있는 옷을 더 챙겨보세요!")

    # ==========================================
    # [5단계] 안전 가이드 및 마무리 (입력 성공 시에만 출력)
    # ==========================================
    print(f"\n{'='*50}")
    print(f" 🛡️ [출국 D-1] {travel_destination} 필수 안전 가이드")
    print(f"{'='*50}")

    travel_info = {
        "일본": {
            "긴급번호": "경찰(110), 구급차/소방(119)",
            "인사말": "스미마셍 (죄송합니다/저기요), 아리가또 고자이마스 (감사합니다)",
            "꿀팁": "110V 전용 돼지코 어댑터를 꼭 챙기세요. 현금 사용이 잦습니다."
        },
        "미국": {
            "긴급번호": "경찰/소방/구급 통합(911)",
            "인사말": "Excuse me (실례합니다), Thank you (감사합니다)",
            "꿀팁": "식당 등에서 15~20%의 팁(Tip) 문화가 있습니다. 밤늦은 외출은 삼가세요."
        },
        "유럽": {
            "긴급번호": "EU 통합 긴급번호(112)",
            "인사말": "Hello / Bonjour (안녕하세요), Thank you / Merci (감사합니다)",
            "꿀팁": "소매치기가 잦은 지역이 있으니 귀중품은 몸 안쪽 가방에 보관하세요."
        }
    }

    info = travel_info.get(travel_destination)

    if info:
        print(f"📞 긴급 연락처 : {info['긴급번호']}")
        print(f"🗣️ 필수 인사말 : {info['인사말']}")
        print(f"💡 트래버 꿀팁 : {info['꿀팁']}")
    else:
        print(f"📞 긴급 연락처 : 전 세계 공통 영사콜센터(+82-2-3210-0404)")
        print(f"🗣️ 필수 인사말 : Hello (안녕하세요), Help me (도와주세요)")
        print(f"💡 트래버 꿀팁 : 여권 사본을 따로 보관하고, 낯선 사람의 호의를 주의하세요.")

    print(f"\n{'='*50}")
    print(f" 🎉 모든 준비 완료! {user_name}님, {travel_destination}에서 안전하고 즐거운 여행 되세요!")
    print(f"{'='*50}")

else:
    # 5번 입력 실패 시 메시지
    print("❌ 입력 횟수를 초과했습니다. 보안 검사를 진행할 수 없어 프로그램을 종료합니다.")
