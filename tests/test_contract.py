from pathlib import Path
S=(Path(__file__).parents[1]/"contracts"/"contract.py").read_text()
def test_roles():
 for x in ("def publish(","def request(","def adjudicate(","only named recipient may request"):assert x in S
def test_bounds():
 for x in ("complete operation vector required","ordered indexes required","ALLOWED","BLOCKED","AMBIGUOUS"):assert x in S
def test_lifecycle():
 for x in ('"CHARTERED"','"REQUESTED"','"DECIDED"',"request already fixed"):assert x in S
def test_no_web_fixture():assert "nondet.web" not in S and "raw.githubusercontent" not in S

