from ord_mediascout_client import (
    ContractStatus,
    ContractSubjectType,
    ContractType,
    CreateFinalContractRequest,
    CreateInitialContractRequest,
    CreateOuterContractRequest,
    DeleteContractWebApiDto,
    DeleteContractKind,
    GetFinalContractsRequest,
    GetInitialContractRequest,
    GetOuterContractsRequest,
)

# Setup test data
_clientId = 'CLoEdAGEwv6EufqiTlkEeIAg'  # «Совкомбанк»
_initial_contract_clientId = 'CLb0sZrPj5Y0KafIDU8ECPIw'  # «Рога и Копыта»
_contractorId = 'CLcnt4AYTax0aLQfxuRZjG_Q'  # «ООО Рафинад»
_finalContractId = 'CTiwhIpoQ_F0OEPpKj8vWKGg'


def test_create_final_contract(client):
    request_data = CreateFinalContractRequest(
        number='AB1234567890C',
        date='2023-03-02',
        amount=100000.00,
        isAgentActingForPublisher=True,
        type=ContractType.ServiceAgreement,
        subjectType=ContractSubjectType.Distribution,
        # actionType=MediationActionType.Contracting,
        parentMainContractId='',
        clientId=_clientId,
    )

    response_data = client.create_final_contract(request_data)
    assert request_data.number == response_data.number
    assert request_data.date == response_data.date
    assert request_data.amount == response_data.amount
    # assert request_data.isAgentActingForPublisher == response_data.isAgentActingForPublisher
    assert request_data.type == response_data.type
    assert request_data.subjectType == response_data.subjectType
    # assert request_data.actionType == response_data.actionType
    # assert request_data.parentMainContractId == response_data.parentMainContractId
    assert request_data.clientId == response_data.clientId
    assert response_data.id is not None
    assert response_data.status == ContractStatus.Created or ContractStatus.Active


def test_get_final_contracts(client):
    request_data = GetFinalContractsRequest(status=ContractStatus.Active)

    response_data = client.get_final_contracts(request_data)

    for final_contract in response_data:
        print(f"{final_contract.id=}")
        assert final_contract.id is not None



def test__delete_final_contract(client):
    _finalContractId = 'CTR5RcpKtdDE23ajEqR4s52g'
    request_data = DeleteContractWebApiDto(contractId=_finalContractId, contractKind=DeleteContractKind.FinalContract)
    print(f"{request_data=}")
    response_data = client.delete_contract(request_data)

    assert response_data.status_code == 204


# curl -X 'DELETE' 'https://demo.mediascout.ru/webapi/v3/contracts/FinalContract/CTiwhIpoQ_F0OEPpKj8vWKGg' -H 'accept: */*'

def test_create_initial_contract(client):
    request_data = CreateInitialContractRequest(
        number='ABC-12345',
        date='2023-04-07',
        amount=155000.00,
        isAgentActingForPublisher=True,
        type=ContractType.ServiceAgreement,
        subjectType=ContractSubjectType.Distribution,
        # actionType=MediationActionType.Contracting,
        parentMainContractId=None,
        contractorId=_contractorId,
        clientId=_initial_contract_clientId,
        finalContractId=_finalContractId,
    )

    response_data = client.create_initial_contract(request_data)

    assert request_data.number == response_data.number
    assert request_data.date == response_data.date
    assert request_data.amount == response_data.amount
    # assert request_data.isAgentActingForPublisher == response_data.isAgentActingForPublisher
    assert request_data.type == response_data.type
    assert request_data.subjectType == response_data.subjectType
    # assert request_data.actionType == response_data.actionType
    assert request_data.parentMainContractId == response_data.parentMainContractId
    assert request_data.contractorId == response_data.contractorId
    assert request_data.clientId == response_data.clientId
    assert request_data.finalContractId == response_data.finalContractId
    assert response_data.id is not None
    assert response_data.status == ContractStatus.Created or ContractStatus.Active


def test_get_initial_contracts(client):
    request_data = GetInitialContractRequest(status=ContractStatus.Active)

    response_data = client.get_initial_contracts(request_data)

    for initial_contract in response_data:
        assert initial_contract.id is not None


def test_create_outer_contract(client):
    request_data = CreateOuterContractRequest(
        number='AB1234567890123CD',
        date='2023-03-05',
        amount=150000.00,
        isAgentActingForPublisher=True,
        type=ContractType.ServiceAgreement,
        subjectType=ContractSubjectType.Distribution,
        # actionType=MediationActionType.Contracting,
        parentMainContractId='',
        contractorId=_clientId,
        isRegReport=True,
    )

    response_data = client.create_outer_contract(request_data)

    assert request_data.number == response_data.number
    assert request_data.date == response_data.date
    assert request_data.amount == response_data.amount
    # assert request_data.isAgentActingForPublisher == response_data.isAgentActingForPublisher
    assert request_data.type == response_data.type
    assert request_data.subjectType == response_data.subjectType
    # assert request_data.actionType == response_data.actionType
    # assert request_data.parentMainContractId == response_data.parentMainContractId
    assert request_data.contractorId == response_data.contractorId
    assert response_data.id is not None
    assert response_data.status == ContractStatus.Created or ContractStatus.Active


def test_get_outer_contracts(client):
    request_data = GetOuterContractsRequest(status=ContractStatus.Active)

    response_data = client.get_outer_contracts(request_data)

    for outer_contract in response_data:
        assert outer_contract.id is not None
