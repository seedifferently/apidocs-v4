# Drop-in UI
The PokitDok Drop-in UI enables anyone to add eligibility checks to their own website with a fully styled and functional UI.

* Patient eligibility in seconds
* One simple drop-in with full customization
* All major insurance carriers
* Detailed info including deductible status and co-pays


## 1. Get Drop-in Token
First you will need to <a href='https://platform.pokitdok.com/signup' target='_blank'>sign up for a PokitDok Platform account</a>
and generate a `Drop-In Token` from the Platform dashboard <a href='https://platform.pokitdok.com/dashboard#/dropin' target='_blank'>Drop-In UI</a> page, where you will need
to provide the hostname of the website where you'll be using the drop-in UI, as well as select the type of drop-in UI widget you'll be using. In regards to the provided hostname
it needs to be the exact page that you intend on embedding the widget (i.e.- `https://pokitdok.com/page/with/widget` not `https://pokitdok.com/`).


## 2. Include JS File

```html
<script src="https://platform.pokitdok.com/static/sdk/pd-dropin.min.js"></script>
```

Include the `pd-dropin.min.js` file in your website.


## 3. Add HTML Container

```html
<div id="dropin-ui"></div>
```

Add an HTML container with a specific ID that will house your drop-in UI.


## 4. Initialize Drop-in

```javascript
pokitdok.dropin('INSERT YOUR DROP-IN TOKEN HERE', {
   container: 'dropin-ui'
   type: 'eligibility'
})
```

Call the `pokitdok.dropin` function, using your PokitDok Platform `Drop-In Token` and <a href='/#options'>options</a>.

The drop-in UI form will auto-populate in the HTML container that you specified, and you can run eligibility checks right away.

## Options

> Example with options:

```javascript
pokitdok.dropin('INSERT YOUR DROP-IN TOKEN HERE', {
    container: 'dropin-ui',
    type: 'eligibility',
    styles: 'styles.css',
    values: {
        'trading_partner_id': 'MOCKPAYER'
    },
    autoSubmit: true,
    onFormSuccess: function() {
        // do stuff here
    },
    onFormLoad: function() {
        // do stuff here
    }
}
```

> Full list of values available to pre-populate:

```javascript
{
    'member': {
        'first_name': 'Jane',
        'last_name': 'Doe',
        // (Insurance Member ID)
        'id': '123456789',
        'birth_date': '1970-01-01'
    }
    'trading_partner_id': 'MOCKPAYER'
}
```

<aside class="warning">
'container' and 'type' are required options for the drop-in UI to work.
</aside>

Name              | Description
------------------|--------------------------------------------------------------------------------------
container         | The id of the HTML container that the drop-in UI will be housed in
type              | The only type of drop-in UI currently supported is `eligibility`
styles            | URL pointing to a css file to override styles with
values            | An object of values that the form will pre-populate with
autoSubmit        | False by default; boolean indicating that form should submit automatically once all fields are filled
onFormSuccess     | Function that gets called when the form has been submitted successfully
onFormLoad        | Function that gets called when the form has been loaded successfully
