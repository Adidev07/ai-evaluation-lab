import time
def answer(question, candidate):
    q=question.lower()
    if candidate not in ('baseline','guarded'):
        raise ValueError('Choose baseline or guarded')
    if candidate=='guarded' and any(x in q for x in ('password','secret','ignore previous')):
        return 'I cannot disclose secrets.'
    knowledge={'refund':'Refunds are available within 30 days.', 'shipping':'Shipping takes 3 to 5 business days.', 'support':'Contact support@example.test.'}
    return next((v for k,v in knowledge.items() if k in q), 'I do not know.')
def run(payload, records):
    candidate=payload.get('candidate','guarded')
    rows=[]
    for case in records:
        start=time.perf_counter()
        response=answer(case['question'],candidate)
        elapsed=round((time.perf_counter()-start)*1000,4)
        passed=case['expected'].lower() in response.lower()
        rows.append(dict(id=case['id'],question=case['question'],response=response,expected=case['expected'],passed=passed,latency_ms=elapsed))
    return dict(candidate=candidate,pass_rate=round(sum(r['passed'] for r in rows)/len(rows),3) if rows else 0, cases=rows, note='Rule-based local candidates; measured latency excludes network and model inference.')
