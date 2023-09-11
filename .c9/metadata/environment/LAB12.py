{"filter":false,"title":"LAB12.py","tooltip":"/LAB12.py","undoManager":{"mark":80,"position":80,"stack":[[{"start":{"row":1,"column":23},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["In the Flow Control module, you learned about if-else statements, while loops, lists, and for loops. Now you will apply what you have learned to the real-world application of human insulin.","","Here, you will use lists, for and while loops, and basic math to calculate the net charge of insulin from pH 0 to pH 14.","","In this lab, you will:","","    Create a dictionary of pKa values (which indicate the strength of an acid) that will be used in the net charge calculations","    Use the count() method to get a count of amino acids","    Use a while loop to calculate the net charge of insulin from pH 0 to pH 14",""],"id":2}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":14,"column":0},"end":{"row":23,"column":29},"action":"insert","lines":["# Python3.6  ","# Coding: utf-8  ","# Store the human preproinsulin sequence in a variable called preproinsulin:  ","preproInsulin = \"malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn\"  ","# Store the remaining sequence elements of human insulin in variables:  ","lsInsulin = \"malwmrllpllallalwgpdpaaa\"  ","bInsulin = \"fvnqhlcgshlvealylvcgergffytpkt\"  ","aInsulin = \"giveqcctsicslyqlenycn\"  ","cInsulin = \"rreaedlqvgqvelgggpgagslqplalegslqkr\"  ","insulin = bInsulin + aInsulin"],"id":4}],[{"start":{"row":23,"column":29},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["pKR = {}"],"id":6}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":18},"action":"insert","lines":["'y': 10.07,"],"id":7}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":[" "],"id":8}],[{"start":{"row":25,"column":19},"end":{"row":25,"column":28},"action":"insert","lines":["'c': 8.18"],"id":9}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["."],"id":10}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"remove","lines":["."],"id":11}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":[","],"id":12}],[{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":[" "],"id":13}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":40},"action":"insert","lines":["'k': 10.53"],"id":14}],[{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"insert","lines":["."],"id":15}],[{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"remove","lines":["."],"id":16}],[{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"insert","lines":[","],"id":17}],[{"start":{"row":25,"column":41},"end":{"row":25,"column":42},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":25,"column":42},"end":{"row":25,"column":51},"action":"insert","lines":["'h': 6.00"],"id":19}],[{"start":{"row":25,"column":51},"end":{"row":25,"column":52},"action":"insert","lines":[","],"id":20}],[{"start":{"row":25,"column":52},"end":{"row":25,"column":53},"action":"insert","lines":[" "],"id":21}],[{"start":{"row":25,"column":53},"end":{"row":25,"column":63},"action":"insert","lines":["'r': 12.48"],"id":22}],[{"start":{"row":25,"column":63},"end":{"row":25,"column":64},"action":"insert","lines":[","],"id":23}],[{"start":{"row":25,"column":64},"end":{"row":25,"column":65},"action":"insert","lines":[" "],"id":24}],[{"start":{"row":25,"column":65},"end":{"row":25,"column":74},"action":"insert","lines":["'d': 3.65"],"id":25}],[{"start":{"row":25,"column":74},"end":{"row":25,"column":75},"action":"insert","lines":[","],"id":26}],[{"start":{"row":25,"column":75},"end":{"row":25,"column":76},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":25,"column":76},"end":{"row":25,"column":85},"action":"insert","lines":["'e': 4.25"],"id":28}],[{"start":{"row":25,"column":86},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":80},"action":"insert","lines":["seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})"],"id":30}],[{"start":{"row":27,"column":80},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":["p"],"id":32},{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"insert","lines":["H"]}],[{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"insert","lines":[" "],"id":33},{"start":{"row":29,"column":3},"end":{"row":29,"column":4},"action":"insert","lines":["="]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":[" "],"id":34},{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["-"]}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"remove","lines":["-"],"id":35}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["="],"id":36}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"remove","lines":["="],"id":37}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["-"],"id":38}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"remove","lines":["-"],"id":39}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["0"],"id":40}],[{"start":{"row":29,"column":6},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["",""]},{"start":{"row":31,"column":0},"end":{"row":31,"column":1},"action":"insert","lines":["w"]}],[{"start":{"row":31,"column":1},"end":{"row":31,"column":2},"action":"insert","lines":["h"],"id":42},{"start":{"row":31,"column":2},"end":{"row":31,"column":3},"action":"insert","lines":["i"]},{"start":{"row":31,"column":3},"end":{"row":31,"column":4},"action":"insert","lines":["l"]},{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":5},"end":{"row":31,"column":6},"action":"insert","lines":[" "],"id":43},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"insert","lines":[")"]}],[{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"remove","lines":[")"],"id":44}],[{"start":{"row":31,"column":6},"end":{"row":31,"column":8},"action":"insert","lines":["()"],"id":45}],[{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"insert","lines":["p"],"id":46},{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":["H"]}],[{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":[" "],"id":47},{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":["<"]},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"insert","lines":[" "],"id":48},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["1"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["3"]}],[{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"remove","lines":[")"],"id":49},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"remove","lines":["3"]}],[{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["4"],"id":50},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":[")"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":[":"]}],[{"start":{"row":31,"column":17},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"insert","lines":["n"],"id":52},{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"insert","lines":["e"]},{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"insert","lines":["t"]},{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"insert","lines":["C"]}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["h"],"id":53},{"start":{"row":32,"column":9},"end":{"row":32,"column":10},"action":"insert","lines":["a"]},{"start":{"row":32,"column":10},"end":{"row":32,"column":11},"action":"insert","lines":["r"]},{"start":{"row":32,"column":11},"end":{"row":32,"column":12},"action":"insert","lines":["g"]},{"start":{"row":32,"column":12},"end":{"row":32,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"insert","lines":[" "],"id":54},{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"insert","lines":[" "],"id":55}],[{"start":{"row":32,"column":16},"end":{"row":32,"column":18},"action":"insert","lines":["()"],"id":56}],[{"start":{"row":32,"column":17},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":33,"column":0},"end":{"row":33,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":32,"column":4},"end":{"row":33,"column":9},"action":"remove","lines":["netCharge = (","        )"],"id":58},{"start":{"row":32,"column":4},"end":{"row":36,"column":43},"action":"insert","lines":["netCharge = (","    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \\","    for x in ['k','h','r']}.values()))","    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \\","    for x in ['y','c','d','e']}.values())))"]}],[{"start":{"row":36,"column":43},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]},{"start":{"row":37,"column":4},"end":{"row":38,"column":0},"action":"insert","lines":["",""]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":42},"action":"insert","lines":["print('{0:.2f}'.format(pH), netCharge)"],"id":60}],[{"start":{"row":38,"column":41},"end":{"row":38,"column":42},"action":"remove","lines":[")"],"id":61}],[{"start":{"row":38,"column":32},"end":{"row":38,"column":41},"action":"remove","lines":["netCharge"],"id":62}],[{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"remove","lines":[" "],"id":63}],[{"start":{"row":38,"column":29},"end":{"row":38,"column":31},"action":"remove","lines":["),"],"id":64}],[{"start":{"row":38,"column":27},"end":{"row":38,"column":29},"action":"remove","lines":["pH"],"id":65}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"remove","lines":["("],"id":66}],[{"start":{"row":38,"column":20},"end":{"row":38,"column":26},"action":"remove","lines":["format"],"id":67}],[{"start":{"row":38,"column":17},"end":{"row":38,"column":20},"action":"remove","lines":["}'."],"id":68}],[{"start":{"row":38,"column":15},"end":{"row":38,"column":17},"action":"remove","lines":["2f"],"id":69}],[{"start":{"row":38,"column":13},"end":{"row":38,"column":15},"action":"remove","lines":[":."],"id":70}],[{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"remove","lines":["0"],"id":71}],[{"start":{"row":38,"column":9},"end":{"row":38,"column":12},"action":"remove","lines":["('{"],"id":72}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":9},"action":"remove","lines":["print"],"id":73}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "],"id":74}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":38},"action":"insert","lines":["print('{0:.2f}'.format(pH), netCharge)"],"id":75}],[{"start":{"row":36,"column":43},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":76},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":42},"action":"insert","lines":["print('{0:.2f}'.format(pH), netCharge)"],"id":77}],[{"start":{"row":37,"column":42},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":78},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":42},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":79},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":10},"action":"insert","lines":["pH +=1"],"id":80}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":38},"action":"remove","lines":["print('{0:.2f}'.format(pH), netCharge)"],"id":81},{"start":{"row":40,"column":4},"end":{"row":41,"column":0},"action":"remove","lines":["",""]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":120.80000000000001,"scrollleft":0,"selection":{"start":{"row":40,"column":0},"end":{"row":40,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1694438691649,"hash":"96a4ff470d56535052b00890ee886b026dfaee2d"}