import json
import xlsxwriter
my_list = [];

names = []

flop_byte = []
flop_time = []

for name in names:
 
    with open(name) as f:
        lines = f.readlines() # list containing lines of file
        columns = [] # To store column names

        i = 1
        ffma = 0
        fadd = 0
        fmul = 0
        memory = 0
        time = 0
        for line in lines:
            words = line.split()
            for i in range(len(words)):
                if(words[i] == "smsp__sass_thread_inst_executed_op_ffma_pred_on.sum"):
                    ffma = ffma + float(words[i+2])
                if(words[i] == "smsp__sass_thread_inst_executed_op_fadd_pred_on.sum"):
                    fadd = fadd + float(words[i+2])
                if(words[i] == "smsp__sass_thread_inst_executed_op_fmul_pred_on.sum"):
                    fmul = fmul + float(words[i+2])
                if(words[i] == "Gbyte"):
                    memory = memory + float(words[i+1])*pow(10,9)
                if(words[i] == "Mbyte"):
                    memory = memory + float(words[i+1])*pow(10,6)
                if(words[i] == "Kbyte"):
                    memory = memory + float(words[i+1])*pow(10,3)
                try:
                    if(words[i] == "usecond"):
                        time = time + float(words[i+1])/1000000
                except:
                    print("error")
                if(words[i] == "msecond"):
                    time = time + float(words[i+1])/1000
    
        flops = fadd + fmul + 2*ffma
        print(name)
        print("  flops : " , flops)
        print("  memory : " , memory)
        print("  time : " , time)
        print("  flop/byte : " , (flops/memory))
        print("  flop/sec : " , (flops/time)/pow(10,12))