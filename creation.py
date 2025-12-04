import psycopg2

# Connexion à la base PYTHON (elle doit déjà exister)
creation = psycopg2.connect(
        database="python",
        host="localhost",
        user="postgres",
        password="29122003",
        port=5432
)

action = creation.cursor()

sql = """
CREATE TABLE IF NOT EXISTS APPRENANT(
    Nom VARCHAR(100),
    Prenom VARCHAR(100),
    Email VARCHAR(100),
    Contact VARCHAR(100),
    Adresse VARCHAR(100),
    CdeFact VARCHAR(100)
);
"""

action.execute(sql)
creation.commit()

print("Table APPRENANT créée avec succès !")

action.close()
creation.close()
