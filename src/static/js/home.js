/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'v1/compute_forecast',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(job_id, pid) {
            let ajax_options = {
                type: 'POST',
                url: 'v1/compute_forecast',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',

                data: JSON.stringify({
                    "cpu_request": "string",
                    "design_block_desc": "string",
                    "design_block_id": "string",
                    "job_id": job_id,
                    "mem_request": "string",
                    "model_id": "11",
                    "project_desc": "string",
                    "project_id": pid,
                    "project_phase": "string",
                    "time_request": "2019-09-29",
                    "tool_cmd": "string",
                    "tool_used": "string"

                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(job_id, pid) {
            let ajax_options = {
                type: 'PUT',
                url: 'v1/compute_forecast' + job_id,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    "cpu_request": "string",
                    "design_block_desc": "string",
                    "design_block_id": "string",
                    "job_id": job_id,
                    "mem_request": "string",
                    "model_id": "11",
                    "project_desc": "string",
                    "project_id": pid,
                    "project_phase": "string",
                    "time_request": "2019-09-29",
                    "tool_cmd": "string",
                    "tool_used": "string"

                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(job_id) {
            let ajax_options = {/v1/compute_forecast
                type: 'DELETE',
                url: 'v1/compute_forecast/' + job_id,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $job_id = $('#job_id'),
        $pid = $('#pid');

    // return the API
    return {
        reset: function() {
            $job_id.val('');
            $pid.val('').focus();
        },
        update_editor: function(job_id, pid) {
            $.val(job_id);
            $pid.val(pid).focus();
        },
        build_table: function(job) {
            let rows = ''

            // clear the table
            $('.job table > tbody').empty();

            // did we get a people array?
            if (job) {
                for (let i=0, l=job.length; i < l; i++) {
                    rows += `<tr><td class="job_id">${job[i].job_id}</td><td class="pid">${job[i].pid}</td><td>${job[i].time_request}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $job_id = $('#job_id'),
        $pid = $('#pid');


    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(job_id, pid) {
        return job_id !== "" && pid !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let job_id = $job_id.val(),
            pid = $pid.val();

        e.preventDefault();

        if (validate(job_id, pid)) {
            model.create(job_id, pid)
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#update').click(function(e) {
        let $job_id = $('#job_id'),
            $pid = $('#pid');

        e.preventDefault();

        if (validate(job_id, pid)) {
            model.update(job_id, pid)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let pid = $pid.val();

        e.preventDefault();

        if (validate('placeholder', pid)) {
            model.delete(pid)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            job_id,
            pid;

        job_id = $target
            .parent()
            .find('td.job_id')
            .text();

        pid = $target
            .parent()
            .find('td.pid')
            .text();

        view.update_editor(job_id, pid);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));

