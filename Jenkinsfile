/**
 * Declarative pipeline for basic builds.
 *
 * Validate with the following command:
 *
 * $ curl -X POST -F "jenkinsfile=<Jenkinsfile" http://jenkins.symbio:8080/pipeline-model-converter/validate
 *
 * To disable a stage, add a "when" block like this.
 *
 * stage('Name') {
 *     when { expression { false } }
 * }
 */

pipeline {

    // Specify the agent requirements for executing this pipeline.

    agent {
        label 'ec2-agent-small'
    }

    options {
        timeout(time: 5, unit: 'MINUTES')
        timestamps()
    }

    stages {

        stage('Bootstrap') {
            steps {
                script {
                    functions = load("infrastructure/jenkins/functions.groovy")
                    functions.bootstrap()
                }
            }
        }

        stage('Analyze') {
            steps {
                script { functions.analyze() }
            }
            post {
                always {
                    script { functions.capture_analysis_reports() }
                }
            }
        }

        stage('Test: Unit') {
            steps {
                script { functions.run_tests('app', 'unit') }
            }
            post {
                unsuccessful {
                    script { functions.capture_pytest_reports() }
                }
            }
        }

        stage('Test: Integration') {
            steps {
                script { functions.run_tests('app', 'integration') }
            }
            post {
                unsuccessful {
                    script { functions.capture_pytest_reports() }
                }
            }
        }

        stage('Test: Functional') {
            steps {
                script {
                    functions.run_tests(
                        'app', 'functional', '',
                        "--workcell-conf=../infrastructure/workcells/ur10b.yaml"
                    )
                }
            }
            post {
                always {
                    script { functions.capture_pytest_reports() }
                }
            }
        }

        stage('Publish') {

            when {
                anyOf {
                    branch "master"
                    branch "release-*"
                }
            }

            steps {
                script {
                    functions.publish_docker_image(
                        env.SBT_IMAGE_REF, functions.get_docker_tag()
                    )
                }
            }
        }
    }

    post {
        always {
            script {
                functions.cleanup_docker_artifacts()
                functions.notify_build_result()
            }
        }
    }
}
