from datetime import datetime

def invoke():
    return f'smart-fit: {datetime.now()}'

def main():
    print(invoke())
    
if __name__ == '__main__':
    main()
