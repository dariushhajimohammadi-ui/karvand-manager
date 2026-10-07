import json
import os

DATA_DIR = "data"
KARVANDS_FILE = os.path.join(DATA_DIR, "karvands.json")
REPORT_FILE = os.path.join(DATA_DIR, "report.json")



def ensure_data_dir():
    """اگر پوشه data وجود نداشت، آن را می‌سازد."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_data():
    """داده‌ها را از فایل JSON می‌خواند. اگر فایل نبود یا خراب بود، ساختار اولیه را می‌سازد."""
    ensure_data_dir()
    default_structure = {
        "bootcamp": {
            "title": "Karvand Python",
            "year": 2026
        },
        "karvands": []
    }
    
    if not os.path.exists(KARVANDS_FILE):
        save_data(default_structure)
        return default_structure
    
    try:
        with open(KARVANDS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # اطمینان از وجود کلیدهای اصلی
            if "karvands" not in data:
                data["karvands"] = []
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        print("\" فایل JSON خراب بود یا خوانده نشد. فایل با ساختار اولیه بازسازی شد.")
        save_data(default_structure)
        return default_structure

def save_data(data):
    """داده‌ها را در فایل JSON ذخیره می‌کند."""
    ensure_data_dir()
    with open(KARVANDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def generate_id(karvands):
    """عددی تولید می کند ID"""
    if not karvands:
        return 1
    return max(k["id"] for k in karvands) + 1

# --- توابع ---

def add_karvand():
    print('-'*50)
    print("\nnew karvand")
    full_name = input("full name: ")
    email = input("email: ")
    city = input("city: ")
    degree = input("degree: ")
    field = input("field: ")
    
    skills = []
    while True:
        skill_name = input("name skills(exit): ")
        if skill_name.lower() == 'exit':
            break
        skill_level = input("level skill: ")
        while True:
            try:
                score = int(input("score(1-100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print("error score (1-100)")
            except ValueError:
                print("enter int")
        
        skills.append({
            "name": skill_name,
            "level": skill_level,
            "score": score
        })

    data = load_data()
    new_id = generate_id(data["karvands"])
    
    new_karvand = {
        "id": new_id,
        "full_name": full_name,
        "email": email,
        "city": city,
        "education": {
            "degree": degree,
            "field": field
        },
        "skills": skills
    }
    
    data["karvands"].append(new_karvand)
    save_data(data)
    print(f"karvand an ID {new_id} added")

def list_karvands():
    print('-'*50)
    print("\nall karvakd ")
    data = load_data()
    karvands = data.get("karvands", [])
    
    if not karvands:
        print("not any karvand")
        return
        
    for k in karvands:
        print(f"\nID: {k['id']}")
        print(f"full name : {k['full_name']}")
        print(f"email: {k['email']}")
        print(f"city: {k['city']}")
        print(f"education: {k['education']['degree']} - {k['education']['field']}")
        print("skills:")
        if not k['skills']:
            print("no skill")
        for s in k['skills']:
            print(f"  - {s['name']} ({s['level']}): {s['score']}")

def search_karvand_by_id():
    print('-'*50)
    print("\nsearch by id ")
    try:
        target_id = int(input("enter id: "))
    except ValueError:
        print("enter int")
        return
        
    data = load_data()
    for k in data["karvands"]:
        if k["id"] == target_id:
            print("\nfound karvand")
            print(f"ID: {k['id']}")
            print(f"full name: {k['full_name']}")
            print(f"email: {k['email']}")
            print(f"city: {k['city']}")
            print(f"education: {k['education']['degree']} - {k['education']['field']}")
            print("skills:")
            for s in k['skills']:
                print(f"  - {s['name']} ({s['level']}): {s['score']}")
            return
            
    print("not found ")

def search_karvand_by_skill():
    print('-'*50)
    print("\nsearch by skill")
    skill_name = input("enter skill: ").strip().lower()
    
    data = load_data()
    found = False
    for k in data["karvands"]:
        for s in k["skills"]:
            if s["name"].lower() == skill_name:
                print(f"\n full name: {k['full_name']} | city: {k['city']} | ID: {k['id']}")
                found = True
                break
                
    if not found:
        print("not found ")

def edit_karvand():
    print('-'*50)
    print("\nedit karvand")
    try:
        target_id = int(input("enter ID: "))
    except ValueError:
        print("enter int")
        return
        
    data = load_data()
    for k in data["karvands"]:
        if k["id"] == target_id:
            print("data:")
            print(f"1. email: {k['email']}")
            print(f"2. city: {k['city']}")
            print(f"3. degree : {k['education']['degree']}")
            print(f"4. field : {k['education']['field']}")
            
            choice = input("enter number(1-4): ")
            if choice == '1':
                k['email'] = input("new email: ")
            elif choice == '2':
                k['city'] = input("new city : ")
            elif choice == '3':
                k['education']['degree'] = input("new degree: ")
            elif choice == '4':
                k['education']['field'] = input("new field: ")
            else:
                print("enter (1-4)")
                return
                
            save_data(data)
            print("edit data ")
            return
            
    print("not found karvand ")

def delete_karvand():
    print('-'*50)
    print("\ndelete karvand")
    try:
        target_id = int(input("enter ID: "))
    except ValueError:
        print("enter int")
        return
        
    data = load_data()
    for i, k in enumerate(data["karvands"]):
        if k["id"] == target_id:
            data["karvands"].pop(i)
            save_data(data)
            print(f"delet karvand an ID {target_id}")
            return
            
    print("not found karvand")

def generate_report():
    print('-'*50)
    print("\nreport")
    data = load_data()
    karvands = data.get("karvands", [])
    
    if not karvands:
        print("no information to report ")
        return
        
    total_karvands = len(karvands)
    total_skills = 0
    total_score = 0
    cities = set()
    unique_skills = set()
    
    for k in karvands:
        cities.add(k['city'])
        for s in k['skills']:
            total_skills += 1
            total_score += s['score']
            unique_skills.add(s['name'])
            
    average_score = total_score / total_skills if total_skills > 0 else 0
    
    report = {
        "total_karvands": total_karvands,
        "total_skills": total_skills,
        "average_skill_score": round(average_score, 2),
        "cities": list(cities),
        "unique_skills": list(unique_skills)
    }
    
    # ذخیره در فایل
    ensure_data_dir()
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=4)
        
    print("\nreport")
    print(f" all karvand: {report['total_karvands']}")
    print(f" all skills: {report['total_skills']}")
    print(f" ave skills score: {report['average_skill_score']}")
    print(f"cities: {', '.join(report['cities'])}")
    print(f" non repetitive skills: {', '.join(report['unique_skills'])}")
    print(f"\nreport sava an  {REPORT_FILE}")

# --- منوی اصلی ---

def main():
    while True:
        print("\n" + "="*30)
        print("management system")
        print("="*30)
        print("1)add karvand")
        print("2)show all karvand")
        print("3)search by ID")
        print("4)search by skill")
        print("5)edit karvand")
        print("6)delet karvand")
        print("7)report")
        print("8) exit")
        
        choice = input("enter your ch: ")
        
        if choice == '1':
            add_karvand()
        elif choice == '2':
            list_karvands()
        elif choice == '3':
            search_karvand_by_id()
        elif choice == '4':
            search_karvand_by_skill()
        elif choice == '5':
            edit_karvand()
        elif choice == '6':
            delete_karvand()
        elif choice == '7':
            generate_report()
        elif choice == '8':
            print("good bye ")
            break
        else:
            print("enter number(1-8)")

if __name__ == "__main__":
    main()