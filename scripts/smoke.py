import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as ca
ca.make_calldata_object=lambda method=None,args=None,kwargs=None:{**({"method":method} if method else {}),**({"args":args} if args else {}),**({"kwargs":kwargs} if kwargs else {})}
R=Path(__file__).parents[1];E=(R.parents[3]/"accounts.env").read_text();k=lambda n:re.search(r'^ACCOUNT_'+str(n)+r'_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',E,re.M).group(1).strip()
a=create_account(account_private_key=k(6));b=create_account(account_private_key=k(7));c1=create_client(chain=studionet,account=a);c2=create_client(chain=studionet,account=b);A=json.loads((R/"deployment.json").read_text())["contractAddress"]
def w(c,n,args):
 h=c.write_contract(address=A,function_name=n,args=args);print(n+"_tx="+str(h),flush=True);r=c.wait_for_transaction_receipt(transaction_hash=h,wait_until="finalized",retries=180,interval=5000,full_transaction=True);L=r.get("consensus_data",{}).get("leader_receipt") or [];L=[L] if isinstance(L,dict) else L;assert r.get("result_name")=="MAJORITY_AGREE" and any(x.get("execution_result")=="SUCCESS" for x in L);return str(h)
i="LIVE-LOCK-"+str(int(time.time()));tx={"publish":w(c1,"publish",[i,b.address,"Research interview archive","Permit analysis only for the published accessibility study and no unrelated profiling.",json.dumps(["Aggregate accessibility themes","Quote de-identified excerpts"]),json.dumps(["Advertising profiles","Identity re-identification"])])};tx["request"]=w(c2,"request",[i,json.dumps(["Aggregate accessibility themes"])]);tx["adjudicate"]=w(c1,"adjudicate",[i]);final=c1.read_contract(address=A,function_name="get_lock",args=[i]);assert final["state"]=="DECIDED" and len(final["verdicts"])==1;(R/"evidence"/"live-run.json").write_text(json.dumps({"id":i,"contract":A,"transactions":tx,"final":final},indent=2)+"\n");print(json.dumps(final,indent=2))

