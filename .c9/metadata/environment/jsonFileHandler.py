{"filter":false,"title":"jsonFileHandler.py","tooltip":"/jsonFileHandler.py","undoManager":{"mark":31,"position":31,"stack":[[{"start":{"row":1,"column":23},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["In this lab, you will:","","    Create a module","    Open a file and load the JSON data it contains using the built-in JSON module of Python","    Parse the JSON structure to access insulin data","    Calculate the rough molecular weight of human insulin using given code (similar to the lab Working with the String Sequence and Numeric Weight of Insulin in Python)",""],"id":2}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":11},"action":"insert","lines":["import json"],"id":3}],[{"start":{"row":10,"column":11},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":27},"action":"insert","lines":["def readJsonFile(fileName):"],"id":6}],[{"start":{"row":12,"column":27},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":20},"action":"insert","lines":["data=\"\"         "],"id":8}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":20},"action":"remove","lines":["    "],"id":9},{"start":{"row":13,"column":12},"end":{"row":13,"column":16},"action":"remove","lines":["    "]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":11},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":16,"column":15},"action":"insert","lines":["    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"],"id":11}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"remove","lines":["    "],"id":13}],[{"start":{"row":13,"column":11},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["t"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["r"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["y"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":[":"]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"insert","lines":["    "],"id":15}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":8},"action":"insert","lines":["    "],"id":16}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":12},"action":"insert","lines":["    "],"id":17}],[{"start":{"row":16,"column":39},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":17,"column":0},"end":{"row":17,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":12},"action":"remove","lines":["    "],"id":19},{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["e"],"id":20},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["x"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["c"]}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["c"],"id":21}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["c"],"id":22},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["e"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["p"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":[" "],"id":23},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["I"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["O"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["E"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["r"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["r"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["o"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":[":"],"id":24}],[{"start":{"row":17,"column":19},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["p"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["r"]},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["i"]},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["n"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":13},"end":{"row":18,"column":15},"action":"insert","lines":["()"],"id":26}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":16},"action":"insert","lines":["\"\""],"id":27}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["C"],"id":28},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["o"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["u"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["l"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":[" "],"id":29},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["n"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["o"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":[" "],"id":30},{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["r"]},{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"insert","lines":["e"]},{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":["a"]},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":[" "],"id":31},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":["f"]},{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["i"]},{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"insert","lines":["l"]},{"start":{"row":18,"column":33},"end":{"row":18,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":25},"action":"remove","lines":["files/"],"id":32}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":19},"end":{"row":15,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"0e17873705251b7ec18842f1f66fd423f2248d0b","timestamp":1694441670247}