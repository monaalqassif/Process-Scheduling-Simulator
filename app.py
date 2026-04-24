from flask import Flask, render_template, request, jsonify
from process import Process
from basic_algorithms import fcfs, sjf
from round_robin import rr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    quantum = int(data.get('quantum', 5))
    raw_processes = data.get('processes',[])

    def get_fresh_processes():
        return [Process(p['id'], int(p['arrival']), int(p['burst']), p['color']) for p in raw_processes]

    p_fcfs, g_fcfs = fcfs(get_fresh_processes())
    p_sjf, g_sjf = sjf(get_fresh_processes())
    p_rr, g_rr = rr(get_fresh_processes(), quantum)

    def calc_averages(procs):
        if not procs: return 0, 0
        aw = sum(p.waiting_time for p in procs) / len(procs)
        at = sum(p.turnaround_time for p in procs) / len(procs)
        return aw, at

    aw_fcfs, at_fcfs = calc_averages(p_fcfs)
    aw_sjf, at_sjf = calc_averages(p_sjf)
    aw_rr, at_rr = calc_averages(p_rr)

    return jsonify({
        "fcfs": {"gantt": g_fcfs, "aw": aw_fcfs, "at": at_fcfs},
        "sjf":  {"gantt": g_sjf,  "aw": aw_sjf,  "at": at_sjf},
        "rr":   {"gantt": g_rr,   "aw": aw_rr,   "at": at_rr}
    })

if __name__ == '__main__':
    app.run(debug=True)