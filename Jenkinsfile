pipeline {
    agent any

    stages {
        stage('execute python') { 
            steps {
                sh 'pip install json2html; python3 file.py; cat outfile.html'
                emailext body: readFile("outfile.html"), mimeType: 'html', subject: 'python pipeline build', to: 'soubhagyarage@gmail.com'
            }
        }
    }
}
