from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        id=1,
        nome_do_produto="Borracha",
        nome_da_empresa="Papelaria Solar",
        data_de_fabricacao="2021-07-04",
        data_de_validade="2029-02-09",
        numero_de_serie="FR48",
        instrucoes_de_armazenamento="Ao abrigo de luz solar"
    )

    assert new_product.id == 1
    assert new_product.nome_do_produto == "Borracha"
    assert new_product.nome_da_empresa == "Papelaria Solar"
    assert new_product.data_de_fabricacao == "2021-07-04"
    assert new_product.data_de_validade == "2029-02-09"
    assert new_product.numero_de_serie == "FR48"
    assert new_product.instrucoes_de_armazenamento == "Ao abrigo de luz solar"
