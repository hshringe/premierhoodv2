from django.db import migrations

SQL = """CREATE PROCEDURE buy_stock(player_id int) 
    AS $$
    BEGIN
	    UPDATE premierhoodv2_player 
        SET  buyCount = buyCount + 1
        WHERE id = player_id;
        COMMIT;
    END;
    $$
    LANGUAGE PLPGSQL;
    """
class Migration(migrations.Migration):
    dependencies = [
        ('premierhoodv2', 'storedProc'),
    ]

    operations = [migrations.RunSQL(SQL)]
