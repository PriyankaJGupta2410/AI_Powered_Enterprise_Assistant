class TicketQueries:

    INSERT_TICKET = """
        INSERT INTO tickets
        (
            issue,
            status
        )
        VALUES
        (
            %s,
            %s
        )
        RETURNING
            ticket_id,
            issue,
            status,
            created_at;
    """


    GET_TICKET_BY_ID = """
        SELECT
            ticket_id,
            issue,
            status,
            created_at
        FROM tickets
        WHERE ticket_id = %s;
    """


    GET_ALL_TICKETS = """
        SELECT
            ticket_id,
            issue,
            status,
            created_at
        FROM tickets
        ORDER BY created_at DESC;
    """


    UPDATE_TICKET_STATUS = """
        UPDATE tickets
        SET
            status = %s
        WHERE
            ticket_id = %s;
    """


    DELETE_TICKET = """
        DELETE
        FROM tickets
        WHERE ticket_id = %s;
    """