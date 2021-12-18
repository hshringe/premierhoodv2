from django.db import migrations

SQL = """
create procedure stock_view(username char)
language plpgsql
as $$
begin
SELECT * FROM premierhoodv2_player tbl1 JOIN
(SELECT stock_id
FROM premierhoodv2_userstocksowned
WHERE username_id = username) tbl2 ON tbl1.id = tbl2.stock_id;
commit;
end;$$
"""


class Migration(migrations.Migration):
    dependencies = [
        ('premierhoodv2', '0009_auto_20211217_1924'),
    ]

    operations = [migrations.RunSQL(SQL)]
