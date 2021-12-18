from django.db import migrations

SQL = """CREATE FUNCTION buy_stock_2(IN player_id int) RETURNS integer
    AS $BODY$
    BEGIN
	    UPDATE premierhoodv2_player 
        SET  premierhoodv2_player.buyCount = premierhoodv2_player.uyCount + 1
        WHERE premierhoodv2_player.id = player_id;
        return player_id;
        COMMIT;
    END;
    $BODY$
    LANGUAGE PLPGSQL;
    """
class Migration(migrations.Migration):
    dependencies = [
        ('premierhoodv2', 'storedProc2'),
    ]

    operations = [migrations.RunSQL(SQL)]