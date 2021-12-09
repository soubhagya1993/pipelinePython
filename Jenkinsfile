pipeline {
    agent any

    stages {
        stage('execute python') { 
            steps {
                    sh 'curl -v -o input1.json http://www.example.com/'
                    sh 'pip install json2html; python3 file.py'
                    
                    emailext attachmentsPattern: 'outfile.html',
                    body: readFile("outfile.html"), 
                    subject: 'python pipeline build',
                    to: 'soubhagyarage@gmail.com'
            }
        }
    }
}
