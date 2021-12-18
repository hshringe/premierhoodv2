from django.db import migrations

SQL = """CREATE FUNCTION sell_stock(IN player_id int) RETURNS integer
    AS $BODY$
    BEGIN
	    UPDATE premierhoodv2_player 
        SET buy_count = buy_count - 1
        WHERE id = player_id;
        return player_id;
        COMMIT;
    END;
    $BODY$
    LANGUAGE PLPGSQL;
    """
class Migration(migrations.Migration):
    dependencies = [
        ('premierhoodv2', '0001_auto_20211217_2309'),
    ]

    operations = [migrations.RunSQL(SQL)]