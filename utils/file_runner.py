from os import system


def output_checker(*args,output,true_output):
    output.seek(0)
    true_output.seek(0)  
    outpu = output.read().strip()
    true_outpu = true_output.read().strip()
    print("Output-"+outpu)
    print("True Output-"+true_outpu)  
    if outpu == true_outpu:
        return True
    else:
        return False
def output_obtainer_cpp(*args,Codes):
      with open('Submissions/submission.cpp','r+') as f:
            code = f.readlines()
            temp_file = open('Submissions/temp.cpp','w+')
            for line in code:
                  temp_file.write(line)

            temp_file.write(Codes)
            temp_file.close()
            system('g++ Submissions/temp.cpp -o Submissions/temp')
            system('Submissions/temp')

def output_obtainer_c(*args,Codes):
      with open('Submissions/submission.c','r+') as f:
            code = f.readlines()
            temp_file = open('Submissions/temp.c','w+')
            for line in code:
                  temp_file.write(line)

            temp_file.write(Codes)
            temp_file.close()
            system('gcc Submissions/temp.c -o Submissions/temp')
            system('Submissions/temp')
            try:
                  system('rm ubmissions/temp')
            except:
                  pass

def output_obtainer_py(*args,Codes):
      with open('Submissions/Temp.py','w') as f:
            f.write(Codes)
            f.close()
      system('python3 Submissions/Submission.py')

def result(*args,output,true_output)->str:
            print(open('Submissions/output.txt').read())
            if output_checker(*args,output=output,true_output=true_output):
                  return "All test case passed"
            else:
                  return "One or many test case failed"
print(result(output=open('Submissions/output.txt'),true_output=open('Submissions/true_output.txt')))