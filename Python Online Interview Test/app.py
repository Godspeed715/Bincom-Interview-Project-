import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('bincom_test.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


# --- Question 1: Individual Polling Unit Results ---
@app.route('/polling_unit', methods=['GET', 'POST'])
def polling_unit_results():
    conn = get_db_connection()

    # 1. Fetch all unique IDs for the dropdown menu
    pu_ids = conn.execute(
        'SELECT DISTINCT polling_unit_uniqueid FROM announced_pu_results'
    ).fetchall()

    results = []
    selected_id = None

    # 2. Check if the user clicked the "Submit" button
    if request.method == 'POST':
        selected_id = request.form.get('pu_id')

        # 3. Fetch results for that specific ID
        results = conn.execute(
            'SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = ?',
            (str(selected_id),)
        ).fetchall()

    conn.close()

    # 4. Send the data to the HTML template
    return render_template('polling_unit.html', results=results, pu_ids=pu_ids, selected_id=selected_id)


# --- Question 2: Summed Total Results for LGA ---
@app.route('/lga_results', methods=['GET', 'POST'])
def lga_results():
    conn = get_db_connection()
    lgas = conn.execute('SELECT lga_id, lga_name FROM lga').fetchall()

    results = None
    selected_lga = None

    if request.method == 'POST':
        lga_id = request.form.get('lga_id')
        selected_lga = conn.execute('SELECT lga_name FROM lga WHERE lga_id = ?', (lga_id,)).fetchone()

        # Query joins PU results with Polling Units to sum by party for the LGA
        query = '''
            SELECT r.party_abbreviation, SUM(r.party_score) as total_score
            FROM announced_pu_results r
            JOIN polling_unit p ON r.polling_unit_uniqueid = CAST(p.uniqueid AS TEXT)
            WHERE p.lga_id = ?
            GROUP BY r.party_abbreviation
        '''
        results = conn.execute(query, (lga_id,)).fetchall()

    conn.close()
    return render_template('lga_results.html', lgas=lgas, results=results, selected_lga=selected_lga)


# --- Question 3: Store New Results ---
@app.route('/add_results', methods=['GET', 'POST'])
def add_results():
    conn = get_db_connection()
    parties = conn.execute('SELECT partyid FROM party').fetchall()

    if request.method == 'POST':
        pu_id = request.form.get('pu_id')
        user = "Admin_User"  # Static for this example

        for party in parties:
            score = request.form.get(f"score_{party['partyid']}")
            conn.execute('''
                INSERT INTO announced_pu_results 
                (polling_unit_uniqueid, party_abbreviation, party_score, entered_by_user, date_entered)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (pu_id, party['partyid'], score, user))

        conn.commit()
        conn.close()
        return redirect(url_for('polling_unit_results', pu_id=pu_id))

    conn.close()
    return render_template('add_results.html', parties=parties)


if __name__ == '__main__':
    app.run(debug=True)