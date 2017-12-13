from app import APP

def main():
    APP.run(debug=True, host='0.0.0.0', threaded=True)

if __name__ == '__main__':
    main()